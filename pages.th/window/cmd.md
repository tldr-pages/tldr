# cmd

> ตัวแปลคำสั่งของ Windows.
> ข้อมูลเพิ่มเติม: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd>.

- เริ่มใช้งานตัวแปลคำสั่งของ Windows:

`cmd`

- รันคำสั่งที่ระบุแล้วปิด:

`cmd /c "{{echo Hello world}}"`

- Execute a specific script:

`cmd {{path\to\script.bat}}`
   
- เรียกใช้คำสั่งที่ระบุ จากนั้นป้อนคำสั่งแบบโต้ตอบ:

`cmd /k "{{echo Hello world}}"`

- ปิดการใช้งานคำสั่ง "echo" :

`cmd /q`

- เปิดหรือปิดส่วนขยายคำสั่ง:

`cmd /e:{{on|off}}`

- เปิดหรือปิดการเติมข้อความอัตโนมัติของไฟล์หรือไดเร็กทอรี:

`cmd /f:{{on|off}}`

- เปิดหรือปิดการขยายตัวแปรสภาพแวดล้อม:

`cmd /v:{{on|off}}`

- บังคับให้เอาต์พุตใช้การเข้ารหัส Unicode:

`cmd /u`
