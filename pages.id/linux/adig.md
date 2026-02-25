# adig

> Cetak informasi yang diterima dari server Domain Name System (DNS).
> Informasi lebih lanjut: <https://manned.org/adig>.

- Tampilkan record A (bawaan) dari DNS untuk hostname:

`adig {{example.com}}`

- Tampilkan output [d]ebugging tambahan:

`adig -d {{example.com}}`

- Hubungkan ke [s]erver DNS tertentu:

`adig -s {{1.2.3.4}} {{example.com}}`

- Gunakan port TCP tertentu untuk terhubung ke server DNS:

`adig -T {{port}} {{example.com}}`

- Gunakan port UDP tertentu untuk terhubung ke server DNS:

`adig -U {{port}} {{example.com}}`
