# pkg_delete

> Hapus pemasangan paket dalam OpenBSD.
> Lihat juga: `pkg_add`, `pkg_info`.
> Informasi lebih lanjut: <https://man.openbsd.org/pkg_delete>.

- Hapus sebuah paket yang terpasang:

`pkg_delete {{nama_paket}}`

- Hapus paket beserta penunjang (dependency) yang juga tidak lagi dipakai:

`pkg_delete -a {{nama_paket}}`

- Tampilkan apa yang terjadi ketika menghapus suatu paket tanpa memprosesnya secara langsung (dry-run):

`pkg_delete -n {{nama_paket}}`
