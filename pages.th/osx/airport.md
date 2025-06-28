# airport

> เครื่องมือสำหรับตั้งค่าเครือข่ายไร้สาย (WLANs, Wi-Fi).
> ข้อมูลเพิ่มเติม: <https://keith.github.io/xcode-man-pages/airport.1.html>

- แสดงสถานะเครือข่ายไร้สายปัจจุบัน:

`airport --getinfo`

- ตรวจจับทราฟฟิกไร้สายบนช่องสัญญาณ 1:

`airport sniff {{1}}`

- สแกนหาเครือข่ายไร้สายที่ใช้งานได้:

`airport --scan`

- ตัดการเชื่อมต่อจากเครือข่าย airport ปัจจุบัน:

`sudo airport --disassociate`
