# ansible

> Atur grup perangkat komputer yang secara jarak jauh melalui SSH. (Gunakan berkas `/etc/ansible/hosts` untuk menambahkan grup atau host baru).
> Beberapa subperintah seperti `ansible galaxy` memiliki dokumentasi terpisah.
> Informasi lebih lanjut: <https://www.ansible.com/>.

- Tampilkan daftar host yang tergabung dalam suatu grup:

`ansible {{grup}} --list-hosts`

- Uji koneksi (ping) kepada grup perangkat tertentu dengan menggunakan [m]odul ping:

`ansible {{grup}} -m ping`

- Tampilkan informasi faktual tentang suatu grup perangkat dengan menggunakan [m]odul setup:

`ansible {{grup}} -m setup`

- Jalankan perintah pada suatu kelompok perangkat melalui [m]odul command dengan kumpulan [a]rgumen:

`ansible {{grup}} -m command -a '{{perintah_saya}}'`

- Jalankan perintah dengan hak akses administratif:

`ansible {{grup}} --become --ask-become-pass -m command -a '{{perintah_saya}}'`

- Jalankan perintah menggunakan berkas [i]nventaris tertentu:

`ansible {{grup}} -i {{file_inventaris}} -m command -a '{{perintah_saya}}'`

- Tampilkan daftar grup dalam sebuah inventaris:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
