# awslogs

> CLI um Log-Gruppen, Streams und Events von Amazon CloudWatch Logs abzurufen.
> Weitere Informationen: <https://github.com/jorgebastida/awslogs>.

- Liste alle Log-Gruppen auf:

`awslogs groups`

- Liste alle bestehenden Streams einer angegebenen Loggruppe auf:

`awslogs streams {{/var/log/syslog}}`

- Rufe alle Logs für jegliche Streams in der angegebenen Log-Gruppe für die letzten 1 bis 2 Stunden ab:

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- Rufe alle Logs für einen bestimmten CloudWatch-Logs Filter-Ausdruck ab:

`awslogs get {{/aws/lambda/meine_lambda_gruppe}} --filter-pattern='{{ERROR}}'`

- Beobachte Logs für jegliche Streams in der angegebenen Log-Gruppe:

`awslogs get {{/var/log/syslog}} ALL --watch`
