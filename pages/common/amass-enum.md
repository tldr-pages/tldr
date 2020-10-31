# amass enum

> Find subdomains of a domain.
> More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

Passively find subdomains of a domain:

`amass enum -passive -d {{domain_name}}`

Find subdomains of a domain and actively verify them:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

Brute force subdomains:

`amass enum -brute -d {{domain_name}}`

Save results to a text file:

`amass enum -o {{output_file}} -d {{domain_name}}`

Save results to a database:

`amass enum -o {{output_file}} -dir {{path/to/database_directory}}`
