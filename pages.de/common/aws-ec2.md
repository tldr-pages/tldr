# aws ec2

> CLI für AWS EC2.
> AWS EC2 stellt eine sichere und skalierbare Einheit in der AWS Cloud zur Verfügung, um ein schnelleres Entwickeln und Ausrollen von Software zu ermöglichen.
> Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Liste Informationen zu einer bestimmten Instanz auf:

`aws ec2 describe-instances --instance-ids {{instanz_id}}`

- Liste Informationen zu allen Instanzen auf:

`aws ec2 describe-instances`

- Liste Informationen zu allen EC2 Volumen auf:

`aws ec2 describe-volumes`

- Lösche ein EC2 Volumen:

`aws ec2 delete-volume --volume-id {{volumen_id}}`

- Erstelle einen Snapshot basierend auf einem EC2 Volumen:

`aws ec2 create-snapshot --volume-id {{volumen_id}}`

- Liste alle verfügbaren AMIs (Amazon Machine Images) auf:

`aws ec2 describe-images`

- Liste alle verfügbaren EC2 Befehle auf:

`aws ec2 help`

- Zeige Hilfe für bestimmte EC2 Unterbefehle an:

`aws ec2 {{unterbefehl}} help`
