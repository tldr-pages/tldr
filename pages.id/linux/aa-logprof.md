# aa-logprof

> Perbarui profil keamanan AppArmor secara interaktif berdasarkan pelanggaran yang tercatat.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-logprof.8>.

- Tinjau dan perbarui profil secara interaktif berdasarkan log sistem:

`sudo aa-logprof`

- Gunakan direktori tertentu untuk profil AppArmor:

`sudo aa-logprof {{[-d|--dir]}} /{{path/ke/profil}}`

- Gunakan file log tertentu alih-alih default:

`sudo aa-logprof {{[-f|--file]}} /{{path/ke/file_log}}`

- Abaikan semua entri log sebelum tanda yang ditentukan:

`sudo aa-logprof {{[-m|--logmark]}} "{{log_marker_text}}"`

- Tampilkan bantuan:

`aa-logprof {{[-h|--help]}}`
