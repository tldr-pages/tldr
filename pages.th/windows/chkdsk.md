# chkdsk
> ความสมบูรณ์ของระบบไฟล์และข้อมูลเมตาของระบบไฟล์บนดิสก์โวลุ่มและแก้ไขข้อผิดพลาดของระบบ
> ข้อมูลเพิ่มเติม: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- ระบุตัวอักษรไดรฟ์ (ตามด้วยเครื่องหมาย colon), mount point, หรือชื่อของไดรฟ์:

`chkdsk {{volume}}`

- แก้ไขข้อผิดพลาดของไดรฟ์ที่เลือก:

`chkdsk {{volume}} /f`

- ปิดการใช้งานไดรฟ์ที่เลือกก่อนการตรวจสอบ:

`chkdsk {{volume}} /x`
Change the log file size to the specified size
- เปลี่ยนขนาดของไฟล์ log เป็นไปตามขนาดที่ระบุ (เฉพาะ NTFS):

`chkdsk /l {{size}}`
