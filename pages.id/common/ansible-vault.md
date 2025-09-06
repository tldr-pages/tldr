# ansible-vault

> Enkripsi dan dekripsi nilai, struktur data, dan file dalam proyek Ansible.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Buat suatu berkas brankas terenkripsi baru dengan permintaan kata sandi:

`ansible-vault create {{nama_berkas_brankas}}`

- Buat file brankas terenkripsi baru menggunakan berkas kunci (kata sandi) brankas untuk mengenkripsinya:

`ansible-vault create --vault-password-file {{nama_berkas_kata_sandi}} {{nama_berkas_brankas}}`

- Enkripsi file yang ada menggunakan berkas kata sandi opsional:

`ansible-vault encrypt --vault-password-file {{nama_berkas_kata_sandi}} {{nama_berkas_brankas}}`

- Enkripsi suatu teks string menggunakan format string terenkripsi standar Ansible, dan menampilkan petunjuk secara interaktif:

`ansible-vault encrypt_string`

- Lihat isi suatu brankas yang terenkripsi, menggunakan berkas kata sandi untuk mendekripsikannya:

`ansible-vault view --vault-password-file {{nama_berkas_kata_sandi}} {{nama_berkas_brankas}}`

- Ganti kunci (kata sandi) pada brankas terenkripsi dengan mendefinisikan berkas kata sandi baru:

`ansible-vault rekey --vault-password-file {{nama_berkas_kata_sandi_lama}} --new-vault-password-file {{nama_berkas_kata_sandi_baru}} {{nama_berkas_brankas}}`
