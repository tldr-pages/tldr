# amass enum

> Egy domain aldomainjeinek keresése. További információ: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Egy domain aldomainjeinek passzív keresése:

`amass enum -passive -d {{domain_name}}`

- Egy tartomány aldomainjeinek keresése és aktív ellenőrzése a megtalált aldomainek feloldására tett kísérlettel:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- Aldomainek nyers erővel történő keresése:

`amass enum -brute -d {{domain_name}}`

- Az eredmények mentése szöveges fájlba:

`amass enum -o {{output_file}} -d {{domain_name}}`

- Az eredmények mentése adatbázisba:

`amass enum -o {{output_file}} -dir {{path/to/database_directory}}`
