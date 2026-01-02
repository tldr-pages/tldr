# rvm

> Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby.
> Informasi lebih lanjut: <https://rvm.io/rvm/cli>.

- Pasang suatu atau beberapa versi Ruby:

`rvm install {{versi1 versi2 ...}}`

- Tampilkan daftar versi-versi Ruby yang terinstal:

`rvm list`

- Gunakan suatu versi Ruby untuk sesi saat ini:

`rvm use {{versi}}`

- Tetapkan versi default Ruby yang akan dipakai:

`rvm --default use {{versi}}`

- Perbarui suatu versi Ruby:

`rvm upgrade {{versi_saat_ini}} {{versi_baru}}`

- Hapus pemasangan versi Ruby namun simpan kode sumbernya:

`rvm uninstall {{versi}}`

- Hapus pemasangan versi Ruby beserta kode sumbernya:

`rvm remove {{versi}}`

- Tampilkan prasyarat piranti lunak tambahan yang perlu dipasang untuk sistem operasi anda:

`rvm requirements`
