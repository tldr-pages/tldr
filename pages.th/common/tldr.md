# tldr

> แสดงตัวอย่างแบบง่ายสำหรับเครื่องมือบน command-line จากโปรเจคท์ tldr-pages.
> ข้อมูลเพิ่มเติม: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>

- แสดงตัวอย่างการใช้งานคำสั่งที่ใช้บ่อย (บอกใบ้นิดนึง: นี่คือเหตุผลที่คุณสนใจใช้บริการของเราใช่ไหมล่ะ!):

`tldr {{command}}`

- แสดงหน้า tldr ของคำสั่ง tar สำหรับระบบปฏิบัติการ Linux:

`tldr {{[-p|--platform]}} {{linux}} {{tar}}`

- ขอความช่วยเหลือการใช้งานคำสั่งย่อยของ Git:

`tldr {{git-checkout}}`

- ปรับปรุงข้อมูล tldr บนเครื่องของคุณให้ทันสมัย (ถ้าเครื่องของคุณรองรับการ caching):

`tldr {{[-u|--update]}}`
