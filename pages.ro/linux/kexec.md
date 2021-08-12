# kexec

> Reporniți direct într-un nucleu nou.

- Încarcă un nou nucleu:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --command-line={{arguments}}`

- Încărcați un nou nucleu cu parametrii curenți de boot:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --reuse-cmdline`

- Execută un nucleu încărcat în prezent:

`kexec -e`

- Descărcaţi nucleul ţintă kexec curent:

`kexec -u`
