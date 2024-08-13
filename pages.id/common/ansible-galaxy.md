# ansible-galaxy

> Buat dan atur peran pengguna (role) Ansible.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Pasang sebuah peran kepada suatu pengguna:

`ansible-galaxy install {{username}}.{{nama_peran}}`

- Buang peran dari suatu pengguna:

`ansible-galaxy remove {{username}}.{{nama_peran}}`

- Tampilkan daftar peran yang tersedia:

`ansible-galaxy list`

- Cari peran berdasarkan nama:

`ansible-galaxy search {{nama_peran}}`

- Terbitkan sebuah peran baru:

`ansible-galaxy init {{nama_peran}}`

- Dapatkan informasi mengenai peran sebuah pengguna:

`ansible-galaxy role info {{username}}.{{nama_peran}}`

- Dapatkan informasi mengenai suatu koleksi:

`ansible-galaxy collection info {{username}}.{{nama_koleksi}}`
