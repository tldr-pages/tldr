# amass enum

> Find subdomains of a domain.
> More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Passively find subdomains of a [d]omain:

`amass enum -passive -d {{domain_name}}`

- Find subdomains of a [d]omain and actively verify them attempting to resolve the found subdomains:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- Do a brute force search for subdomains:

`amass enum -brute -d {{domain_name}}`

- Save the results to a text file:

`amass enum -o {{output_file}} -d {{domain_name}}`

- Save the results to a database:

`amass enum -o {{output_file}} -dir {{path/to/database_directory}}`
