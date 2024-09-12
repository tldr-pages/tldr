# read

> Shell builtin voor het ophalen van data van `stdin`.
> Meer informatie: <https://manned.org/read.1p>.

- Sla gegevens op die je van het toetsenbord typt:

`read {{variable}}`

- Laat backslash (\\) niet optreden als een escape-teken:

`read -r {{variable}}`

- Lees `stdin` of een bestand en voer een actie uit op elke regel:

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{/dev/stdin|pad/naar/bestand|...}}`
