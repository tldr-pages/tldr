# choco install

> Pasang suatu atau beberapa paket dengan Chocolatey.
> Beberapa subperintah termasuk `install`, `upgrade`, `pin` memiliki dokumentasi terpisah.
> Informasi lebih lanjut: <https://docs.chocolatey.org/en-us/choco/commands/install/>.

- Pasang suatu atau beberapa paket yang dipisahkan oleh spasi:

`choco install {{nama_paket}}`

- Mutakhirkan pemasangan suatu paket:

`choco upgrade {{nama_paket}}`

- Mutakhirkan seluruh paket lawas dan lakukan persetujuan pemasangan secara otomatis:

`choco upgrade all {{[-y|--yes]}}`

- Hapus pemasangan suatu paket dan lakukan persetujuan penghapusan secara otomatis:

`choco uninstall {{nama_paket}} {{[-y|--yes]}}

- Cari suatu paket berdasarkan nama atau kata kunci

`choco search {{query}}`

- Tampilkan daftar seluruh paket yang terpasang dalam perangkat:

`choco list`

- Tampilkan daftar paket lawas yang diketahui memiliki versi terbaru:

`choco outdated`

- Pasang suatu paket dari suatu [s]umber secara spesifik:

`choco install {{nama_paket}} {{[-s|--source]}} {{sumber}}`
