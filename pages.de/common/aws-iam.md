# aws iam

> CLI für AWS IAM.
> Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Liste aller Benutzer auf:

`aws iam list-users`

- Liste aller Richtlinien auf:

`aws iam list-policies`

- Liste aller Gruppen auf:

`aws iam list-groups`

- Liste aller Benutzer zu einer Gruppe auf:

`aws iam get-group --group-name {{gruppe}}`

- Liste einer IAM Richtlinie detailliert auf:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{richtlinie}}`

- Liste alle Zugriffsschlüssel auf:

`aws iam list-access-keys`

- Liste alle Zugriffsschlüssel für einen Benutzer auf:

`aws iam list-access-keys --user-name {{benutzername}}`

- Zeige die AWS IAM Hilfeseite (beinhaltet auch Hinweise für alle Unterbefehle):

`aws iam help`
