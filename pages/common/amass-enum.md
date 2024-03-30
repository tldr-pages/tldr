# amass enum

> Find subdomains of a domain.
> More information: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Find (passively) subdomains of a [d]omain:

`amass enum -d {{domain_name}}`

- Find subdomains of a [d]omain and actively verify them attempting to resolve the found subdomains:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- Do a brute force search for sub[d]omains:

`amass enum -brute -d {{domain_name}}`

- Save the results to a text file:

`amass enum -o {{output_file}} -d {{domain_name}}`

- Save terminal output to a file and other detailed output to a directory:

`amass enum -o {{output_file}} -dir {{path/to/directory}} -d {{domain_name}}`

- List all available data sources:

`amass enum -list`
