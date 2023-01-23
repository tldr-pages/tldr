# gixy

> Az nginx konfigurációs fájljainak elemzése. További információ: <https://github.com/yandex/gixy>.

- Analyze nginx configuration (alapértelmezett elérési út: `/etc/nginx/nginx.conf`):

`gixy`

- Az nginx konfiguráció elemzése, de bizonyos tesztek kihagyása:

`gixy --skips {{http_splitting}}`

- Analyze nginx configuration with the specific severity level:

`gixy {{-l|-ll|-lll}}`

- Analyze nginx configuration files on the specific path (nginx konfigurációs fájlok elemzése az adott elérési útvonalon):

`gixy {{path/to/configuration_file_1}} {{path/to/configuration_file_2}}`
