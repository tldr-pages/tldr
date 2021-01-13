# aws-vault

> Ein Tresor für Entwicklungsumgebungen um AWS Sicherheitsschlüssel sicher speichern und abrufen zu können.
> Mehr Informationen: <https://github.com/99designs/aws-vault>.

- Sicherheitsschlüssel als Profil zu einem Tresor hinzufügen:

`aws-vault add {{profile}}`

- Ausführen eines Kommandos mit AWS Sicherheitsschlüsseln aus dem angegebenen Profil:

`aws-vault exec {{profile}} -- {{aws s3 ls}}`

- Öffnen eines Browser Fensters für den Login in die AWS Konsole:

`aws-vault login {{profile}}`

- Auflistung aller Profile zusammen mit deren Sicherheitsschlüsseln und Sitzungen:

`aws-vault list`

- Rotierung der AWS Sicherheitsschlüssel für ein Profil:

`aws-vault rotate {{profile}}`

- Entfernen von Sicherheitsschlüsseln eines Profils aus dem Tresor:

`aws-vault remove {{profile}}`
