# automountd

> daemon สำหรับการ mount/unmount อัตโนมัติของ `autofs` ที่ถูกเริ่มต้นโดย `launchd` เมื่อจำเป็น.
> ไม่ควรเรียกใช้งานด้วยตนเอง.
> ข้อมูลเพิ่มเติม: <https://keith.github.io/xcode-man-pages/automountd.8.html>

- เริ่ม daemon:

`automountd`

- บันทึกข้อมูลเพิ่มเติมลงใน `syslog`:

`automountd -v`
