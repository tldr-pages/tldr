# asr

> กู้คืน (คัดลอก) ดิสก์อิมเมจไปยังวอลุ่ม.
> ชื่อคำสั่งย่อมาจาก Apple Software Restore.
> ข้อมูลเพิ่มเติม: <https://keith.github.io/xcode-man-pages/asr.8.html>

- กู้คืนอิมเมจดิสก์ไปยังวอลุ่มเป้าหมาย:

`sudo asr restore --source {{อิมเมจไฟล์.dmg}} --target {{ทาง/ไป/วอลุมไฟล์}}`

- ลบข้อมูลในวอลุ่มเป้าหมายก่อนการกู้คืน:

`sudo asr restore --source {{อิมเมจไฟล์.dmg}} --target {{ทาง/ไป/วอลุมไฟล์}} --erase`

- ข้ามขั้นตอนตรวจสอบหลังการกู้คืน:

`sudo asr restore --source {{อิมเมจไฟล์.dmg}} --target {{ทาง/ไป/วอลุมไฟล์}} --noverify`

- โคลนวอลุ่มโดยไม่ใช้อิมเมจดิสก์ตัวกลาง:

`sudo asr restore --source {{ทาง/ไป/วอลุมไฟล์}} --target {{ทาง/ไป/วอลุมไฟล์}}`
