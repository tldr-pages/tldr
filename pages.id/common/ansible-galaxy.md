# ansible-galaxy

> Buat dan atur peran pengguna (role) Ansible.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Tampilkan daftar peran atau koleksi yang tersedia:

`ansible-galaxy {{role|collection}} list`

- Cari suatu peran berdasarkan nama menggunakan tingkat verbositas tertentu (`-v` harus dimasukkan pada akhir baris perintah):

`ansible-galaxy role search {{nama_peran}} -v{{vvvvv}}`

- Pasang atau bongkar peran-peran pengguna:

`ansible-galaxy role {{install|remove}} {{nama_peran1 nama_peran2 ...}}`

- Terbitkan sebuah peran baru:

`ansible-galaxy role init {{nama_peran}}`

- Dapatkan informasi mengenai suatu peran:

`ansible-galaxy role info {{nama_peran}}`

- Pasang atau bongkar kumpulan koleksi (collection):

`ansible-galaxy collection {{install|remove}} {{nama_koleksi1 nama_koleksi1 ...}}`

- Tampilkan bantuan mengenai manajemen peran (role) maupun koleksi (collection):

`ansible-galaxy {{role|collection}} {{[-h|--help]}}`
