# aws iam

> Kommandozeilen Werkzeug für AWS IAM.
> Mehr Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Zeige die AWS IAM Hilfe Seite (beinhaltet auch Hinweise für alle Unter-Kommandos):

`aws iam help`

- Auflistung aller Benutzer:

`aws iam list-users`

- Auflistung aller Richtlinien:

`aws iam list-policies`

- Auflistung aller Gruppen:

`aws iam list-groups`

- Auflistung aller Benutzer zu einer Gruppe:

`aws iam get-group --group-name {{group_name}}`

- Detail-Auflistung einer IAM Richtlinie:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- Auflistung aller Zugriffsschlüssel:

`aws iam list-access-keys`

- Auflistung der Zugriffsschlüssel für einen Benutzer:

`aws iam list-access-keys --user-name {{user_name}}`
