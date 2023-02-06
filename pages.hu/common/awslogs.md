# awslogs

> Csoportok, adatfolyamok és események lekérdezése az Amazon CloudWatch naplóiból. További információ: <https://github.com/jorgebastida/awslogs>.

- Naplócsoportok listázása:

`awslogs groups`

- A megadott csoport meglévő adatfolyamainak listázása:

`awslogs streams {{/var/log/syslog}}`

- A megadott csoportba tartozó, 1 és 2 órával ezelőtti összes folyam naplójának lekérdezése:

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- Egy adott CloudWatch naplók szűrőmintának megfelelő naplók lekérdezése:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'`

- A megadott csoportba tartozó bármely folyam naplóinak figyelése:

`awslogs get {{/var/log/syslog}} ALL --watch`
