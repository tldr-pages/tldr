# sshfs

> Klien sistem berkas (filesystem) berbasis SSH.
> Informasi lebih lanjut: <https://github.com/libfuse/sshfs>.

- Kaitkan (mount) direktori jarak jauh (remote directory):

`sshfs {{nama_pengguna}}@{{host_jarak_jauh}}:{{direktori_jarak_jauh}} {{titik_kait}}`

- Lepaskan (unmount) direktori jarak jauh (remote directory):

`umount {{titik_kait}}`

- Kaitkan direktori jarak jauh (remote directory) dari server dengan port spesifik:

`sshfs {{nama_pengguna}}@{{host_jarak_jauh}}:{{direktori_jarak_jauh}} -p {{2222}}`

- Gunakan kompresi:

`sshfs {{nama_pengguna}}@{{host_jarak_jauh}}:{{direktori_jarak_jauh}} -C`

- Ikuti tautan simbolik (symbolic links):

`sshfs -o follow_symlinks {{nama_pengguna}}@{{host_jarak_jauh}}:{{direktori_jarak_jauh}} {{titik_kait}}`
