# chgrp

> Ubah hak kepemilikan grup pengguna dalam sistem operasi untuk kumpulan berkas dan direktori.
> Lihat juga: `chown`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- Gantikan grup pemilik suatu berkas/direktori:

`chgrp {{grup}} {{jalan/menuju/berkas_atau_direktori}}`

- Gantikan grup pemilik suatu direktori beserta seluruh berkasnya secara rekursif:

`chgrp {{[-R|--recursive]}} {{grup}} {{jalan/menuju/direktori}}`

- Gantikan grup pemilik berkas tautan pintas simbolik (symbolic link):

`chgrp {{[-h|--no-dereference]}} {{grup}} {{jalan/menuju/pintas_symlink}}`

- Ganti kepemilikan grup untuk suatu berkas/direktori berdasarkan berkas acuan rancangan kepemilikan yang ditentukan:

`chgrp --reference {{jalan/menuju/berkas_acuan}} {{jalan/menuju/berkas_atau_direktori}}`
