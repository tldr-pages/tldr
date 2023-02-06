# amass db

> Kölcsönhatás egy Amass-adatbázissal. További információ: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Az adatbázisban lévő összes elvégzett felsorolás listázása:

`amass db -dir {{path/to/database_directory}} -list`

- Megadott felsorolási index és tartománynév eredményeinek megjelenítése:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -show`

- Egy domain összes talált aldomainjének listázása egy felsoroláson belül:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -names`

- Összefoglaló megjelenítése a talált aldomainekről egy felsoroláson belül:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -summary`
