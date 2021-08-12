# debman

> Citiți paginile om din pachetele dezinstalate.
> Mai multe informaţii: <https://manpages.debian.org/latest/debian-goodies/debman.1.html>

- Citiți o pagină om pentru o comandă care este furnizată de un nume de pachet specificat:

`debman -p {{package_name}} {{command_name}}`

- Specificați o versiune de pachet pentru a descărca:

`debman -p {{package_name}}={{version}} {{command_name}}`

- Citiți o pagină de om într-un fișier `.deb`:

`debman -f {{path/to/filename.deb}} {{command_name}}`
