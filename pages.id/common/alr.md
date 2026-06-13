# alr

> Manajer paket untuk Ada.
> Atur toolchain, kebergantungan, alat, dan pustaka proyek Ada.
> Informasi lebih lanjut: <https://alire.ada.dev/docs/#first-steps>.

- Buat suatu proyek biner atau pustaka:

`alr init {{--bin|--lib}} {{nama_proyek}}`

- Tambahkan suatu pustaka (crate) sebagai kebergantungan proyek saat ini:

`alr add {{crate}}`

- Jalankan file biner yang telah terkompilasi (tidak usah untuk melakukan `build` sebelumnya):

`alr run`

- Lakukan kompilasi terhadap kode sumber proyek:

`alr build {{--release|--development|--validation}}`
