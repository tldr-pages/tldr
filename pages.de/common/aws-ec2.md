# aws ec2

> Kommandozeilen Werkzeug für AWS EC2.
> AWS EC2 stellt eine sichere und skalierbare Einheit in der AWS Cloud zur Verfügung um ein schnelleres Entwickeln und Ausrollen von Software zu ermöglichen.
> Mehr Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Auflistung aller verfügbaren EC2 Kommandos:

`aws ec2 help`

- Anzeigen einer Hilfe für bestimmte EC2 Unter-Kommandos:

`aws ec2 {{subcommand}} help`

- Auflistung von Informationen zu einer bestimmten Instanz:

`aws ec2 describe-instances --instance-ids {{instance_id}}`

- Auflistung von Informationen zu allen Instanzen:

`aws ec2 describe-instances`

- Auflistung von Informationen zu allen EC2 Volumen:

`aws ec2 describe-volumes`

- Auflistung von Informationen zu einem einzigen EC2 Volumen:

`aws ec2 delete-volume --volume-id {{volume_id}}`

- Erstellung eines Snapshots basierend auf einem EC2 Volumen:

`aws ec2 create-snapshot --volume-id {{volume_id}}`

- Auflistung aller verfügbaren AMIs (Amazon Machine Images):

`aws ec2 describe-images`
