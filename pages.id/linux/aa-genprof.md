# aa-genprof

> Buat profil keamanan AppArmor dengan memantau perilaku program.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- Mulai buat profil untuk sebuah program:

`sudo aa-genprof {{path/ke/program}}`

- Tentukan direktori kustom untuk profil:

`sudo aa-genprof {{[-d|--dir]}} /{{path/ke/profil}} {{path/ke/program}}`

- Tentukan file log kustom untuk profiling:

`sudo aa-genprof {{[-f|--file]}} /{{path/ke/file_log}} {{path/ke/program}}`

- Tampilkan bantuan:

`aa-genprof {{[-h|--help]}}`
