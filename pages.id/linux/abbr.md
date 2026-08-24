# abbr

> Kelola singkatan untuk fish shell.
> Kata yang didefinisikan pengguna diganti dengan frasa yang lebih panjang setelah dimasukkan.
> Informasi lebih lanjut: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Tambahkan singkatan baru:

`abbr {{[-a|--add]}} {{abbreviation_name}} {{command}} {{command_arguments}}`

- Ganti nama singkatan yang sudah ada:

`abbr --rename {{old_name}} {{new_name}}`

- Hapus singkatan yang sudah ada:

`abbr {{[-e|--erase]}} {{abbreviation_name}}`

- Impor singkatan yang didefinisikan pada host lain melalui SSH:

`ssh {{host_name}} abbr {{[-s|--show]}} | source`
