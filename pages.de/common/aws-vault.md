# aws-vault

> Ein Tresor für Entwicklungsumgebungen, um AWS Sicherheitsschlüssel sicher speichern und abrufen zu können.
> Weitere Informationen: <https://github.com/99designs/aws-vault>.

- Füge einen Sicherheitsschlüssel als Profil zu einem Tresor hinzu:

`aws-vault add {{profil}}`

- Führe einen Befehl mit AWS Sicherheitsschlüsseln aus dem angegebenen Profil aus:

`aws-vault exec {{profil}} -- {{aws s3 ls}}`

- Öffne ein Browserfenster für den Login in die AWS Konsole:

`aws-vault login {{profil}}`

- Liste alle Profile zusammen mit deren Sicherheitsschlüsseln und Sitzungen auf:

`aws-vault list`

- Rotiere die AWS Sicherheitsschlüssel für ein Profil:

`aws-vault rotate {{profil}}`

- Entferne Sicherheitsschlüsseln eines Profils aus dem Tresor:

`aws-vault remove {{profil}}`
