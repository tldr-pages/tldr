# ansible-doc

> Tampilkan informasi mengenai modul-modul (action plugins) yang terpasang dalam pustaka pemasangan Ansible.
> Tampilkan informasi singkat mengenai daftar plugin beserta deskripsi singkatnya.
> Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Tampilkan daftar modul/plugin yang tersedia:

`ansible-doc {{[-l|--list]}}`

- Tampilkan daftar modul/plugin berdasarkan jenisnya:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{[-l|--list]}}`

- Tampilkan informasi mengenai suatu modul/plugin:

`ansible-doc {{nama_plugin}}`

- Tampilkan informasi mengenai suatu modul/plugin berdasarkan jenis spesifiknya:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{nama_plugin}}`

- Lihat contoh cara penggunaan (dalam playbook) bagi suatu modul/plugin:

`ansible-doc {{[-s|--snippet]}} {{nama_plugin}}`

- Tampilkan informasi mengenai suatu plugin/modul dalam format JSON:

`ansible-doc {{[-j|--json]}} {{nama_plugin}}`
