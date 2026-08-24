# aa-genprof

> Buat profil keamanan AppArmor dengan memantau perilaku program.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- Mulai buat profil untuk sebuah program:

`sudo aa-genprof {{program_path}}`

- Tentukan direktori kustom untuk profil:

`sudo aa-genprof {{[-d|--dir]}} /{{path/ke/profil}} {{program_path}}`

- Tentukan file log kustom untuk profiling:

`sudo aa-genprof {{[-f|--file]}} /{{path/ke/file_log}} {{program_path}}`

- Tampilkan bantuan:

`aa-genprof {{[-h|--help]}}`
