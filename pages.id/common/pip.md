# pip

> Pengelola paket Python.
> Beberapa subperintah seperti `install` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://pip.pypa.io>.

- Memasang paket:

`pip install {{nama_paket}}`

- Memasang versi paket tertentu:

`pip install {{nama_paket}}=={{versi_paket}}`

- Memasang paket untuk hanya digunakan oleh pengguna saat ini:

`pip install --user {{nama_paket}}`

- Meningkatakan paket ke versi terbaru:

`pip install --upgrade {{nama_paket}}`

- Mencopot pemasangan paket:

`pip uninstall {{nama_paket}}`

- Menyimpan daftar paket terpasang ke berkas:

`pip freeze > {{requirements.txt}}`

- Memasang paket dari berkas:

`pip install --requirement {{requirements.txt}}`

- Menampilkan informasi paket terpasang:

`pip show {{nama_paket}}`
