# aa-decode

> Dekode log audit AppArmor menjadi format yang dapat dibaca manusia.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- Dekode string heksadesimal:

`aa-decode {{hexstring}}`

- Dekode file log:

`sudo aa-decode {{logfile}}`

- Dekode log dari `stdin` (contoh: file yang dialihkan/ redirected):

`sudo aa-decode - < {{logfile}}`

- Tampilkan bantuan:

`aa-decode {{[-h|--help]}}`
