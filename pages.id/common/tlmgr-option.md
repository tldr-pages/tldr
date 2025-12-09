# tlmgr option

> Modul pengaturan TeX Live.
> Informasi lebih lanjut: <https://www.tug.org/texlive/doc/tlmgr.html#option>.

- Tampilkan seluruh pengaturan TeX Live:

`tlmgr option showall`

- Tampilkan seluruh pengaturan yang telah diatur:

`tlmgr option show`

- Tampilkan seluruh pengaturan TeX Live dalam format JSON:

`tlmgr option showall --json`

- Tampilkan nilai terhadap suatu butir pengaturan TeX Live:

`tlmgr option {{pengaturan}}`

- Ubah nilai atas suatu butir pengaturan TeX Live:

`tlmgr option {{pengaturan}} {{nilai}}`

- Atur TeX Live untuk mendapatkan pembaruan daring dalam masa depan, setelah dipasang melalui media DVD:

`tlmgr option {{repository}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`
