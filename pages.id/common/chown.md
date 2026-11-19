# chown

> Ubah hak kepemilikan pengguna dan grup pengguna dalam sistem operasi terhadap kumpulan berkas dan direktori.
> Lihat juga: `chgrp`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Gantikan kepemilikan suatu berkas kepada pengguna tertentu:

`sudo chown {{pengguna}} {{jalan/menuju/berkas_atau_direktori}}`

- Gantikan kepemilikan suatu berkas kepada pengguna tertentu, beserta grup pengguna yang menaunginya:

`sudo chown {{pengguna}}:{{group}} {{jalan/menuju/berkas_atau_direktori}}`

- Gantikan kepemilikan menggunakan nama pengguna dan nama grup `pengguna` yang sama:

`sudo chown {{pengguna}}: {{jalan/menuju/berkas_atau_direktori}}`

- Gantikan grup pemilik suatu berkas/direktori di mana pengguna saat ini juga bergabung dalam grup pengguna tersebut:

`chown :{{grup}} {{jalan/menuju/berkas_atau_direktori}}`

- Gantikan pemilik suatu direktori beserta seluruh berkasnya secara rekursif:

`sudo chown {{[-R|--recursive]}} {{pengguna}} {{path/to/directory}}`

- Gantikan pemilik berkas tautan pintas simbolik (symbolic link):

`sudo chown {{[-h|--no-dereference]}} {{pengguna}} {jalan/menuju/pintas_symlink}}`

- Ganti kepemilikan untuk suatu berkas/direktori berdasarkan berkas acuan rancangan kepemilikan yang ditentukan:

`sudo chown --reference {{jalan/menuju/berkas_acuan}} {{jalan/menuju/berkas_atau_direktori}}`
