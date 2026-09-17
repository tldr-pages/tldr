# csvsql

> Hasilkan pernyataan SQL untuk sebuah file CSV atau jalankan pernyataan tersebut secara langsung pada sebuah basis data (database).
> Bagian dari csvkit.
> Informasi lebih lanjut: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Hasilkan sebuah pernyataan SQL CREATE TABLE untuk sebuah file CSV:

`csvsql {{jalan/menuju/data.csv}}`

- Impor sebuah file CSV ke dalam sebuah basis data SQL:

`csvsql --insert --db "{{mysql://pengguna:kata_sandi@host/basis_data}}" {{jalan/menuju/data.csv}}`

- Jalankan sebuah kueri (query) SQL pada sebuah file CSV:

`csvsql --query "{{select * from 'data'}}" {{jalan/menuju/data.csv}}`
