# ansible-pull

> Tarik buku-buku aturan main (playbook) dari suatu repositori sistem manajemen versi (VCS), dan jalankan tugas-tugasnya bagi host lokal.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Tarik suatu playbook dari repositori VCS, kemudian jalankan aturan default dari playbook local.yml:

`ansible-pull -U {{url_repositori}}`

- Tarik suatu playbook dari repositori VCS, kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U {{url_repositori}} {{playbook}}`

- Tarik suatu playbook dari [C]abang tertentu pada repositori VCS, kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U {{url_repositori}} -C {{cabang}} {{playbook}}`

- Tarik suatu playbook dari repositori VCS, kemudian definisikan daftar perangkat/host dari suatu berkas (hosts), kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U {{url_repositori}} -i {{berkas_hosts}} {{playbook}}`
