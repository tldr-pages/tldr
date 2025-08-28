# ansible-lint

> Terapkan aturan dan rekomendasi praktik terbaik terhadap konten otomasi Anda.
> Informasi lebih lanjut: <https://ansible.readthedocs.io/projects/lint/>.

- Terapkan terhadap suatu playbook dan direktori peran:

`ansible-lint {{jalan/menuju/berkas_playbook}} {{jalan/menuju/direktori_peran}}`

- Terapkan terhadap suatu playbook kecuali kumpulan peraturan tertentu:

`ansible-lint {{[-x|--exclude-rules]}} {{peraturan1,peraturan2,...}} {{jalan/menuju/berkas_playbook}}`

- Terapkan terhadap suatu playbook dalam mode luring (offline), dan atur luaran perintah dalam format PEP8:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{jalan/menuju/berkas_playbook}}`

- Terapkan terhadap suatu playbook menggunakan suatu direktori peraturan:

`ansible-lint {{[-r|--rules]}} {{jalan/menuju/direktori_peraturan_kustom}} {{jalan/menuju/berkas_playbook}}`

- Terapkan terhadap seluruh konten Ansible, secara rekursif, dalam suatu direktori:

`ansible-lint {{jalan/menuju/direktori_proyek}}`
