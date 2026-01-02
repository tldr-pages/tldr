# pip

> Pengelola paket Python.
> Beberapa subperintah seperti `install` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://pip.pypa.io/en/stable/cli/pip/>.

- Pasang suatu paket (lihat dokumentasi `pip install` untuk melihat contoh pemasangan tambahan):

`pip install {{nama_paket}}`

- Pasang suatu paket untuk hanya digunakan oleh pengguna saat ini:

`pip install --user {{nama_paket}}`

- Tingkatkan suatu paket ke versi terbaru:

`pip install {{[-U|--upgrade]}} {{nama_paket}}`

- Copot pemasangan suatu paket:

`pip uninstall {{nama_paket}}`

- Simpan daftar paket-paket terpasang ke dalam suatu berkas:

`pip freeze > {{requirements.txt}}`

- Tampilkan informasi suatu paket yang terpasang:

`pip show {{nama_paket}}`

- Pasang kumpulan paket dari suatu berkas:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
