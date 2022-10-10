# clamdscan

> โปรแกรมแสกนหาไวรัสบนคอมมานด์ไลน์ โดยใช้โปรแกรมพื้นหลัง ClamAV
> ข้อมูลเพิ่มเติม: <https://www.clamav.net>.

- แสกนข้อบกพร่องของไฟล์หรือไฟล์ในไดเรคทอรี

`clamdscan {{path/to/file_or_directory}}`

- แสกนข้อมูลจากสตรีมอินพุทมาตรฐาน

`{{command}} | clamdscan -`

- แสกนไดเรคทอรีปัจจุบันแล้วแสดงผลไฟล์ที่ตรวจพบความบกพร่อง

`clamdscan --infected`

- ส่งผลการแสกนไปยังไฟล์ที่ระบุ

`clamdscan --log {{path/to/log_file}}`

- ย้ายไฟล์ที่พบการติดไวรัสไปยังไดเรคทอรีที่ระบุ

`clamdscan --move {{path/to/quarantine_directory}}`

- ลบไฟล์ที่พบการติดไวรัส

`clamdscan --remove`

- ใช้มัลติเธรดในการตรวจไดเรคทอรี

`clamdscan --multiscan`

- ส่งตัวอธิบายไฟล์ไปยังโปรแกรมแสกนพื้นหลังแทนการส่งไฟล์ข้อมูล

`clamdscan --fdpass`
