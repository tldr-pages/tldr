# alembic

> Alat migrasi pangkalan data untuk SQLAlchemy.
> Informasi lebih lanjut: <https://manned.org/alembic>.

- Inisialisasikan Alembic dalam suatu proyek:

`alembic init {{jalan/menuju/direktori}}`

- Buatu sebuah berkas skrip migrasi dengan fitur generasi migrasi otomatis:

`alembic revision --autogenerate -m "{{pesan}}"`

- Lakukan proses pemutakhiran pangkalan data menuju struktur terkini:

`alembic upgrade head`

- Turunkan pangkalan data menuju satu revisi sebelumnya:

`alembic downgrade -1`

- Tampilkan daftar riwayat migrasi:

`alembic history`
