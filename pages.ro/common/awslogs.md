# awslogs

> Interogări grupuri, fluxuri și evenimente din jurnalele Amazon CloudWatch.
> Mai multe informaţii: <https://github.com/jorgebastida/awslogs>

- Lista de grupuri jurnal:

`awslogs groups`

- Listează fluxurile existente pentru grupul specificat:

`awslogs streams {{/var/log/syslog}}`

- Obțineți jurnale pentru orice fluxuri din grupul specificat între 1 și 2 ore în urmă:

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- Obțineți jurnale care se potrivesc cu un anumit model de filtrare CloudWatch Logs:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'`

- Urmăriți jurnalele pentru orice fluxuri din grupul specificat:

`awslogs get {{/var/log/syslog}} ALL --watch`
