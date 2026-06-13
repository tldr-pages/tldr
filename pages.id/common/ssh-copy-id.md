# ssh-copy-id

> Pasang kunci publik Anda di berkas/fail authorized_keys pada mesin jarak jauh (remote host).
> Informasi lebih lanjut: <https://manned.org/ssh-copy-id>.

- Salin kunci Anda ke mesin jarak jauh (remote host):

`ssh-copy-id {{nama_pengguna}}@{{host_jarak_jauh}}`

- Salin kunci publik yang diberikan ke mesin jarak jauh (remote host):

`ssh-copy-id -i {{lokasi/ke/kunci_publik}} {{nama_pengguna}}@{{host_jarak_jauh}}`

- Salin kunci publik yang diberikan ke mesin jarak jauh (remote host) dengan port spesifik:

`ssh-copy-id -i {{lokasi/ke/kunci_publik}} -p {{port}} {{nama_pengguna}}@{{host_jarak_jauh}}`
