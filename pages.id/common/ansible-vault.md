# ansible-vault

> Lakukan proses enkripsi (persandian) dan dekripsi terhadap nilai, struktur data, dan berkas dalam proyek Ansible.
> Informasi lebih lanjut: <https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>.

- Buat suatu berkas brankas terenkripsi baru dengan memasukkan kata sandi pada prompt masukan berikutnya:

`ansible-vault create {{jalan/menuju/berkas_brankas}}`

- Sunting, lihat, atau ganti kunci enkripsi terhadap suatu berkas brankas terenkripsi dengan memasukkan kata sandi pada prompt masukan berikutnya:

`ansible-vault {{edit|view|rekey}} {{jalan/menuju/berkas_brankas}}`

- Buat suatu berkas brankas terenkripsi baru menggunakan berkas kunci (kata sandi) brankas untuk mengenkripsinya:

`ansible-vault create --vault-password-file {{jalan/menuju/berkas_kata_sandi}} {{jalan/menuju/berkas_brankas}}`

- Sandikan suatu berkas teks yang ada menggunakan berkas kata sandi opsional:

`ansible-vault encrypt --vault-password-file {{jalan/menuju/berkas_kata_sandi}} {{jalan/menuju/berkas_brankas}}`

- Sandikan suatu teks string menggunakan format string terenkripsi standar Ansible, dan menampilkan petunjuk secara interaktif:

`ansible-vault encrypt_string`

- Lihat isi suatu brankas yang terenkripsi, menggunakan berkas kata sandi untuk membukanya:

`ansible-vault view --vault-password-file {{jalan/menuju/berkas_kata_sandi}} {{jalan/menuju/berkas_brankas}}`

- Ganti kunci (kata sandi) pada brankas terenkripsi dengan membuat suatu berkas kata sandi baru:

`ansible-vault rekey --vault-password-file {{jalan/menuju/berkas_kata_sandi_lama}} --new-vault-password-file {{jalan/menuju/berkas_kata_sandi_baru}} {{jalan/menuju/berkas_brankas}}`
