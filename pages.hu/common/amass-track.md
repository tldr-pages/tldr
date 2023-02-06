# amass track

> Ugyanazon tartomány felsorolásai közötti különbségek nyomon követése. További információ: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- A megadott tartomány két utolsó felsorolása közötti különbség megjelenítése:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -last 2`

- Megjeleníti a különbséget egy adott időpont és az utolsó felsorolás között:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -since {{01/02 15:04:05 2006 MST}}`
