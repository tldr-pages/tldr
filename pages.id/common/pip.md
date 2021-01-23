# pip

> Pengelola paket Python.
> Informasi lebih lanjut: <https://pip.pypa.io>.

- Memasang paket:

`pip install {{nama_paket}}`

- Memasang versi paket tertentu:

`pip install {{nama_paket}}=={{versi_paket}}`

- Meningkatakan paket ke versi terbaru:

`pip install -U {{nama_paket}}`

- Mencopot pemasangan paket:

`pip uninstall {{nama_paket}}`

- Menyimpan daftar paket terpasang ke berkas:

`pip freeze > {{requirements.txt}}`

- Memasang paket dari berkas:

`pip install -r {{requirements.txt}}`

- Menampilkan informasi paket terpasang:

`pip show {{nama_paket}}`
