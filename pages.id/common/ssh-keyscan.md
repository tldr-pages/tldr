# ssh-keyscan

> Mengambil kunci publik SSH dari host jarak jauh (remote host).
> Informasi lebih lanjut: <https://man.openbsd.org/ssh-keyscan>.

- Mengambil semua kunci publik SSH dari sebuah host jarak jauh (remote host):

`ssh-keyscan {{nama_host}}`

- Mengambil semua kunci publik SSH dari host jarak jauh (remote host) yang berjalan pada port tertentu:

`ssh-keyscan -p {{port}} {{nama_host}}`

- Mengambil tipe kunci publik SSH tertentu dari sebuah host jarak jauh (remote host):

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{nama_host}}`

- Perbarui berkas/fail `known_hosts` SSH secara manual dengan sidik jari (fingerprint) dari host yang diberikan:

`ssh-keyscan -H {{nama_host}} >> ~/.ssh/known_hosts`
