# aiac

> ใช้ OpenAI ผลิตการกำหนดค่าของ IaC, เครื่องมือ , คิวรีสำหรับค้นหา และอื่นๆ.
> ข้อมูลเพิ่มเติม: <https://github.com/gofireflyio/aiac>

- สร้าง Terraform สำหรับบัญชี Azure storage:

`aiac get terraform {{for an azure storage account}}`

- สร้าง Dockerfile สำหรับ nginx:

`aiac get dockerfile {{for a secured nginx}}`

- สร้าง GitHub Action ที่จะใช้ Terraform ร่วม:

`aiac get github action {{that plans and applies terraform}}`

- สร้างโค้ด Python สำหรับสแกนพอร์ตที่เปิดทั้งหมดในเครือข่ายของฉัน:

`aiac get python {{code that scans all open ports in my network}}`

- สร้างคิวรี MongoDB ที่รวมเอกสารทั้งหมดตามวันที่สร้าง:

`aiac get mongo {{query that aggregates all documents by created date}}`
