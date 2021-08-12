# amass enum

> Găsiți subdomenii ale unui domeniu.
> Mai multe informaţii: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>

- Găsirea pasivă a subdomeniilor unui domeniu:

`amass enum -passive -d {{domain_name}}`

- Găsiți subdomenii ale unui domeniu și verificați-le în mod activ încercarea de a rezolva subdomeniile găsite:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- Face o căutare de forță brută pentru subdomenii:

`amass enum -brute -d {{domain_name}}`

- Salvați rezultatele într-un fișier text:

`amass enum -o {{output_file}} -d {{domain_name}}`

- Salvați rezultatele într-o bază de date:

`amass enum -o {{output_file}} -dir {{path/to/database_directory}}`
