# chcon

> Modificați contextul de securitate SELinux al unui fișier sau fișierele/directoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/chcon>

- Vizualizarea contextului de securitate al unui fișier:

`ls -lZ {{path/to/file}}`

- Modificați contextul de securitate al unui fișier țintă, utilizând un fișier de referință:

`chcon --reference={{reference_file}} {{target_file}}`

- Modificați întregul context de securitate SELinux al unui fișier:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- Modificați doar partea de utilizator a contextului de securitate SELinux:

`chcon -u {{user}} {{filename}}`

- Modificați doar partea de rol a contextului de securitate SELinux:

`chcon -r {{role}} {{filename}}`

- Modificați numai partea de tip a contextului de securitate SELinux:

`chcon -t {{type}} {{filename}}`

- Modificaţi doar zona de intervală/nivel a contextului de securitate SELinux:

`chcon -l {{range/level}} {{filename}}`
