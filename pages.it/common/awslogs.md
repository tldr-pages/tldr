# awslogs

> Interroga gruppi, stream ed eventi dai log Amazon CloudWatch.
> Maggiori informazioni: <https://github.com/jorgebastida/awslogs#options>.

- Elenca i gruppi di log:

`awslogs groups`

- Elenca gli stream esistenti per il gruppo specificato:

`awslogs streams {{/var/log/syslog}}`

- Ottieni log per qualsiasi stream nel gruppo specificato tra 1 e 2 ore fa:

`awslogs get {{/var/log/syslog}} {{[-s|--start]}} '{{2h ago}}' {{[-e|--end]}} '{{1h ago}}'`

- Ottieni log che corrispondono a un pattern di filtro CloudWatch Logs specifico:

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern '{{ERROR}}'`

- Osserva i log per qualsiasi stream nel gruppo specificato:

`awslogs get {{/var/log/syslog}} ALL --watch`
