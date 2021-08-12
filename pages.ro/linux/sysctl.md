# sysctl

> Listați și modificați variabilele de execuție a kernel-ului.

- Afișează toate variabilele disponibile și valorile acestora:

`sysctl -a`

- Setați o variabilă de stare a kernel-ului modificabilă:

`sysctl -w {{section.tunable}}={{value}}`

- Obțineți în prezent manipulatoare de fișiere deschise:

`sysctl fs.file-nr`

- Obțineți limita pentru fișierele deschise simultan:

`sysctl fs.file-max`

- Aplicați modificările de la `/etc/sysctl.conf`:

`sysctl -p`
