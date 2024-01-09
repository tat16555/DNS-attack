# DNS-Fender
# รายละเอียด

DNS-Fender เป็นเครื่องมือที่ออกแบบมาเพื่อทำโจมตีแบบ DNS Amplification โดยใช้ข้อมูล Resolver ที่ได้จาก Shodan. โปรแกรมนี้ถูกพัฒนาขึ้นโดยใช้ Python และสนับสนุนการใช้งานในระบบปฏิบัติการ Windows.


## การขยาย DNS

มีสองเกณฑ์สำหรับเวกเตอร์การโจมตีด้วยการขยายสัญญาณที่ดี: 1) การสืบค้นสามารถตั้งค่าด้วยที่อยู่ต้นทางที่ถูกปลอมแปลง (เช่น ผ่านโปรโตคอลเช่น ICMP หรือ UDP ที่ไม่จำเป็นต้องมีการจับมือกัน); และ 2) การตอบสนองต่อแบบสอบถามมีขนาดใหญ่กว่าแบบสอบถามอย่างมาก DNS เป็นแพลตฟอร์มอินเทอร์เน็ตหลักที่แพร่หลายซึ่งตรงตามเกณฑ์เหล่านี้ ดังนั้นจึงกลายเป็นแหล่งที่มาของการโจมตีแบบขยายสัญญาณที่ใหญ่ที่สุด

โดยทั่วไปแล้ว การสืบค้น DNS จะถูกส่งผ่าน UDP ซึ่งหมายความว่า เช่นเดียวกับการสืบค้น ICMP ที่ใช้ในการโจมตี SMURF การสืบค้นจะเริ่มทำงานและลืมไป เป็นผลให้แอตทริบิวต์แหล่งที่มาสามารถปลอมแปลงได้และผู้รับไม่สามารถระบุความจริงก่อนที่จะตอบสนองได้

![enter image description here](https://lh3.googleusercontent.com/pw/ABLVV86-GQWUb1orWA7KwTzX5rZARXS5V5ejdj68rspcF5qFsdcVruiug3A4rPejIBxBYVWnTyufkh-CtvD9OYsDcpl8T6J5_bKNJblClDTXNGqhnyKyb6B7mCmkevk_W02DpJTjO934wF3xnliqqyu112Ce=w761-h652-s-no-gm?authuser=0)

# ความต้องการ
- Python 3.x   （`ไม่รองรับการใช้ Python 2.x หรือ เวอร์ชั่นที่ต่ำกว่า`）
- Shodan API Key
- Shodan CLI (คำสั่ง `shodan`)

## การติดตั้ง

1. ติดตั้ง Python 3.x จาก [เว็บไซต์หลักของ Python](https://www.python.org/).
2. รันคำสั่ง `pip install -r requirements.txt` เพื่อติดตั้ง dependencies
	```bash
	pip install -r requirements.txt
	```

## การใช้งาน

 1. #### เปิดหน้าต่าง command prompt:
	 สำหรับ Windows:
	```bash
	-   กด `Windows + R` เพื่อเปิดหน้าต่าง "Run".
	-   พิมพ์ `cmd` แล้วกด Enter.
	```
	สำหรับ macOS: 
	```bash
	-   กด `Command + Space` เพื่อเปิด Spotlight Search แล้วพิมพ์ "Terminal" แล้วกด Enter.
	```
	สำหรับ Linux: 
	```bash
	-   สามารถเปิดได้จากเมนู "Applications" หรือ "System Tools" หรือค้นหา "Terminal" ได้ตามระบบที่คุณใช้.
	```	
	
 2. #### change directory ไปยังโฟลเดอร์ที่ติดตั้ง DNS-Fender
	 สำหรับ Windows:
	```bash
	- cd C:\path\to\your\folder
	```
	สำหรับ macOS: 
	```bash
	- cd ~/Documents/path/to/your/folder
	```
	สำหรับ Linux: 
	```bash
	-	cd /path/to/your/folder
	```
 4. #### รันโปรแกรมโดยใช้คำสั่ง:
	```bash
	python  DNS-Fender.py  -k  <api_key>  -t  <target_host>
	```

	โดยที่  <api_key>  เป็น  Shodan  API  key  และ  <target_host>  เป็น  Target  IP  หรือ
	Website.

โครงสร้างโฟลเดอร์

 - DNS-Fender.py ： ไฟล์ที่ใช้สั่งโจม
 - attack_report.txt :  ไฟล์รายงานการโจมตีทั้งหมด.
 - detailed_attack_report.txt :  ไฟล์รายงานการโจมตีที่ละเอียด.
 - DNS-Resolvers.txt :  ไฟล์ที่บันทึก  Resolver  IPs  ที่ได้จาก  Shodan.

หมายเหตุ

โปรแกรมนี้ถูกพัฒนาเพื่อการศึกษาและทดสอบเท่านั้น.  การนำไปใช้ในทางที่ผิดกฎหมายหรือไม่สุจริตทางกฎหมาย  ไม่ได้รับการสนับสนุน.

ผู้จัดทำ
[Pannatat]

**หากคุณต้องการเพิ่มฟีเจอร์หรือแก้ไขข้อผิดพลาด**
> กรุณาสร้าง  Pull  Request  หรือติดต่อผู้จัดทำ.

# ข้อกำหนดและเงื่อนไข
โปรแกรมนี้ได้รับการพัฒนาขึ้นเพื่อให้บริการเพื่อการศึกษาและทดสอบเท่านั้น. การนำไปใช้ในทางที่ผิดกฎหมายหรือไม่สุจริตทางกฎหมาย ไม่ได้รับการสนับสนุน. 
## การใช้งาน โปรแกรมนี้เป็น Open Source และตามข้อกำหนดใน [LICENSE.md](LICENSE.md). 
1. คุณสามารถดาวน์โหลดและใช้โปรแกรมนี้ได้ฟรี. 
2. คุณไม่ได้รับอนุญาตให้นำโปรแกรมนี้ไปใช้ในทางที่ผิดกฎหมายหรือไม่สุจริตทางกฎหมาย. 
3. ผู้จัดทำไม่รับผิดชอบต่อความเสียหายที่อาจเกิดขึ้นจากการใช้โปรแกรมนี้. 
### Contributing หากคุณต้องการเพิ่มฟีเจอร์หรือแก้ไขข้อผิดพลาด, กรุณาสร้าง Pull Request หรือติดต่อผู้จัดทำ. 
### ข้อตกลงและเงื่อนไขการใช้งาน การใช้งานโปรแกรมนี้ถือว่าคุณยอมรับข้อตกลงและเงื่อนไขทั้งหมดที่ระบุในไฟล์นี้.




# Details

DNS-Fender is a tool designed for DNS Amplification attacks using Resolver data obtained from Shodan. The program is developed using Python and supports operation on the Windows operating system.

## DNS Amplification

There are two criteria for a good amplification vector: 1) the query can be set with a spoofed source address (e.g., through protocols like ICMP or unnecessary UDP handshake); and 2) the response to the query is much larger than the query itself. DNS is the predominant Internet platform that fulfills these criteria, making it the source of the largest amplification attacks.

Generally, DNS queries are sent via UDP, which means, similar to ICMP queries used in SMURF attacks, the query is initiated and then forgotten. This results in the source address attribute being forgeable, and the recipient cannot determine the veracity before responding.

![enter image description here](https://lh3.googleusercontent.com/pw/ABLVV86-GQWUb1orWA7KwTzX5rZARXS5V5ejdj68rspcF5qFsdcVruiug3A4rPejIBxBYVWnTyufkh-CtvD9OYsDcpl8T6J5_bKNJblClDTXNGqhnyKyb6B7mCmkevk_W02DpJTjO934wF3xnliqqyu112Ce=w761-h652-s-no-gm?authuser=0)

# Requirements
- Python 3.x (`Not compatible with Python 2.x or versions below`)
- Shodan API Key
- Shodan CLI (Command `shodan`)

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Run the command `pip install -r requirements.txt` to install dependencies.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. #### Open a command prompt window:
   For Windows:
    ```bash
    - Press `Windows + R` to open the "Run" window.
    - Type `cmd` and press Enter.
    ```
   For macOS:
    ```bash
    - Press `Command + Space` to open Spotlight Search and type "Terminal," then press Enter.
    ```
   For Linux:
    ```bash
    - Open from the "Applications" or "System Tools" menu, or search for "Terminal" based on your system.
    ```

2. #### Change directory to the folder where DNS-Fender is installed:
   For Windows:
    ```bash
    - cd C:\path\to\your\folder
    ```
   For macOS:
    ```bash
    - cd ~/Documents/path/to/your/folder
    ```
   For Linux:
    ```bash
    - cd /path/to/your/folder
    ```

4. #### Run the program using the command:
    ```bash
    python DNS-Fender.py -k <api_key> -t <target_host>
    ```

    Where `<api_key>` is your Shodan API key, and `<target_host>` is the Target IP or Website.

Folder Structure

 - DNS-Fender.py: The file used to initiate attacks.
 - attack_report.txt: The file containing all attack reports.
 - detailed_attack_report.txt: The file containing detailed attack reports.
 - DNS-Resolvers.txt: The file that records Resolver IPs obtained from Shodan.

Note

This program is developed for educational and testing purposes only. Usage for any illegal or unethical purposes is not supported.

Author
[Pannatat]

**If you want to add features or fix bugs**
> Please create a Pull Request or contact the developer.

# Terms and Conditions
This program is developed for educational and testing purposes only. Usage for any illegal or unethical purposes is not supported. 
## Usage
This program is Open Source and subject to the terms in [LICENSE.md](LICENSE.md). 
1. You can download and use this program for free. 
2. You are not allowed to use this program for any illegal or unethical purposes. 
3. The developer is not responsible for any damage that may arise from using this program. 
### Contributing
If you want to add features or fix bugs, please create a Pull Request or contact the developer. 
### Terms and Conditions of Use
The use of this program constitutes acceptance of all terms and conditions specified in this file.



