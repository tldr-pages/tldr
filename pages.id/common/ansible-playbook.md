# ansible-playbook

> Jalankan kumpulan tugas yang didefinisikan di dalam buku aturan main (playbook), kepada para mesin secara jarak jauh melalui SSH.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Jalankan kumpulan tugas yang didefinisikan dalam buku aturan main (playbook):

`ansible-playbook {{playbook}}`

- Jalankan kumpulan tugas playbook dengan [i]nventaris mesin secara kustom:

`ansible-playbook {{playbook}} -i {{berkas_inventaris}}`

- Jalankan kumpulan tugas playbook dengan variabel [e]kstra sebagaimana didefinisikan dalam barisan perintah (command-line):

`ansible-playbook {{playbook}} -e "{{variabel1}}={{nilai1}} {{variabel2}}={{nilai2}}"`

- Jalankan kumpulan tugas playbook dengan variabel [e]kstra sebagaimana didefinisikan di dalam suatu berkas JSON:

`ansible-playbook {{playbook}} -e "@{{daftar_variabel.json}}"`

- Jalankan kumpulan tugas playbook dengan konfigurasi tag tertentu:

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- Jalankan kumpulan tugas playbook, dimulai dari nama tugas spesifik:

`ansible-playbook {{playbook}} --start-at {{nama_tugas}}`

- Jalankan kumpulan tugas playbook tanpa melakukan perubahan sebenarnya (dry-run):

`ansible-playbook {{playbook}} --check --diff`
