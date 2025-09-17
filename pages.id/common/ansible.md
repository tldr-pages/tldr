# ansible

> Atur grup perangkat komputer yang secara jarak jauh melalui SSH. (Gunakan berkas `/etc/ansible/hosts` untuk menambahkan grup atau host baru).
> Beberapa subperintah seperti `ansible galaxy` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Tampilkan daftar host yang tergabung dalam suatu grup:

`ansible {{grup}} --list-hosts`

- Uji koneksi (ping) kepada grup perangkat tertentu dengan menggunakan [m]odul ping:

`ansible {{grup}} {{[-m|--module-name]}} ping`

- Tampilkan informasi faktual tentang suatu grup perangkat dengan menggunakan [m]odul setup:

`ansible {{grup}} {{[-m|--module-name]}} setup`

- Jalankan perintah pada suatu kelompok perangkat melalui [m]odul command dengan kumpulan [a]rgumen:

`ansible {{grup}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{perintah_saya}}'`

- Jalankan perintah dengan hak akses administratif:

`ansible {{grup}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{perintah_saya}}'`

- Jalankan perintah menggunakan berkas [i]nventaris tertentu:

`ansible {{grup}} {{[-i|--inventory]}} {{file_inventaris}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{perintah_saya}}'`

- Tampilkan daftar grup dalam sebuah inventaris:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
