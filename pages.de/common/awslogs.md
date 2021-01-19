# awslogs

> Kommandozeilen Werkzeug um Log Gruppen, Streams und Events von Amazon Cloudwatch Logs abzurufen:
> Mehr Informationen: <https://github.com/jorgebastida/awslogs>.

- Auflisten aller Log Gruppen:

`awslogs groups`

- Auflisten aller bestehenden Streams einer angegebenen Log Gruppe:

`awslogs streams {{/var/log/syslog}}`

- Abrufen aller logs für jegliche Streams in der angegebenen Log Gruppe für die letzten 1 bis 2 Stunden:

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- Abrufen aller Logs für einen bestimmten Cloudwatch Logs Filter Ausdruck:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'`

- Beobachten der Logs für jegliche Streams in der angegebenen Log Gruppe:

`awslogs get {{/var/log/syslog}} ALL --watch`
