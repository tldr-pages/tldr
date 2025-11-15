# git check-attr

> Tampilkan daftar jalur direktori (pathname) beserta atribut internal Git (gitattribute) yang diasosiasikan terhadap direktori tersebut.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-check-attr>.

- Tampilkan informasi seluruh atribut Git dalam suatu berkas:

`git check-attr --all {{jalan/menuju/berkas}}`

- Cek nilai suatu atribut Git dalam suatu berkas:

`git check-attr {{atribut}} {{jalan/menuju/berkas}}`

- Cek nilai seluruh atribut Git dalam kumpulan berkas:

`git check-attr --all {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Cek nilai suatu atribut Git dalam kumpulan berkas:

`git check-attr {{atribut}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`
