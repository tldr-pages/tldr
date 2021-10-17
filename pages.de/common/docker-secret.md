# docker secret

> Verwalte Secrets für Docker Swarm.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Erstelle ein neues Secret über die Standardeingabe:

`{{befehl}} | docker secret create {{secret_name}} -`

- Erstelle ein neues Secret aus einer Datei:

`docker secret create {{secret_name}} {{pfad/zur/datei}}`

- Liste alle Secrets auf:

`docker secret ls`

- Zeige detaillierte Informationen zu einem oder mehreren Secrets in einem menschenlesbaren Format:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Lösche eines oder mehrere Secrets:

`docker secret rm {{secret_name1 secret_name2 ...}}`
