# ansible-inventory

> Tampilkan dan simpan informasi suatu inventaris Ansible (inventory).
> Lihat juga: `ansible`.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Tampilkan informasi inventaris default:

`ansible-inventory --list`

- Tampilkan suatu inventaris kustom:

`ansible-inventory --list --inventory {{jalan/menuju/berkas_atau_skrip_atau_direktori}}`

- Tampilkan informasi inventaris default dalam format YAML:

`ansible-inventory --list --yaml`

- Simpan informasi inventaris default ke dalam suatu berkas teks:

`ansible-inventory --list --output {{jalan/menuju/berkas}}`
