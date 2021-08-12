# dpkg

> Manager de pachete Debian.
> Mai multe informaţii: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>

- Instalați un pachet:

`dpkg -i {{path/to/file.deb}}`

- Elimină un pachet:

`dpkg -r {{package_name}}`

- Lista pachetelor instalate:

`dpkg -l {{pattern}}`

- Listați conținutul pachetului:

`dpkg -L {{package_name}}`

- Lista conţinutului unui pachet local:

`dpkg -c {{path/to/file.deb}}`

- Aflați ce pachet deține un fișier:

`dpkg -S {{filename}}`
