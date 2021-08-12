# gixy

> Analizați fișierele de configurare nginx.
> Mai multe informaţii: <https://github.com/yandex/gixy>

- Analizați configurația nginx (calea implicită: `/etc/nginx/nginx.conf`):

`gixy`

- Analizați configurația nginx, dar săriți teste specifice:

`gixy --skips {{http_splitting}}`

- Analizați configurația nginx cu nivelul specific de severitate:

`gixy {{-l|-ll|-lll}}`

- Analizați fișierele de configurare nginx pe calea specifică:

`gixy {{path/to/configuration_file_1}} {{path/to/configuration_file_2}}`
