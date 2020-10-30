# pip3

> Pengelola paket Python.
> Informasi lebih lanjut: <https://pip.pypa.io>.

- Menemukan paket tersedia:

`pip3 search {{nama_paket}}`

- Memasang paket:

`pip3 install {{nama_paket}}`

- Memasang versi paket tertentu:

`pip3 install {{nama_paket}}=={{versi_paket}}`

- Meningkatkan paket ke versi terbaru:

`pip3 install --upgrade {{nama_paket}}`

- Mencopot pemasangan paket:

`pip3 uninstall {{nama_paket}}`

- Menyimpan daftar paket terpasang ke berkas:

`pip3 freeze > {{requirements.txt}}`

- Memasang paket dari berkas:

`pip3 install --requirements {{requirements.txt}}`

- Menampilkan informasi paket terinstal:

`pip3 show {{nama_paket}}`
