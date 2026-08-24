# aa-mergeprof

> Gabungkan file profil keamanan AppArmor ke dalam direktori profil.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-mergeprof.8>.

- Gabungkan satu atau lebih file profil ke dalam direktori profil default:

`sudo aa-mergeprof {{file1 file2 ...}}`

- Gabungkan file profil ke dalam direktori tertentu:

`sudo aa-mergeprof {{[-d|--dir]}} /{{path/ke/profil}} {{file1 file2 ...}}`

- Tampilkan bantuan:

`aa-mergeprof {{[-h|--help]}}`
