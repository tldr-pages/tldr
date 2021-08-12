# mycli

> Un client de linie de comandă pentru MySQL care poate efectua auto-completare și evidențierea sintaxei.
> Mai multe informaţii: <https://mycli.net>

- Conectarea la o bază de date locală de pe portul 3306, utilizând numele de utilizator curent al utilizatorului:

`mycli {{database_name}}`

- Conectarea la o bază de date (utilizatorul va fi solicitat pentru o parolă):

`mycli -u {{username}} {{database_name}}`

- Conectați-vă la o bază de date pe o altă gazdă:

`mycli -h {{database_host}} -P {{port}} -u {{username}} {{database_name}}`
