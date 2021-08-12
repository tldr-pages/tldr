# aws cur

> Creați, interogați și ștergeți definițiile raportului de utilizare AWS.
> Mai multe informaţii: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>

- Creați o definiție a raportului de cost și utilizare AWS dintr-un fișier JSON:

`aws cur put-report-definition --report-definition file://{{path/to/report-definition.json}}`

- definițiile raportului de utilizare a listei definite pentru contul conectat:

`aws cur describe-report-definitions`

- Ștergeți o definiție a raportului de utilizare:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
