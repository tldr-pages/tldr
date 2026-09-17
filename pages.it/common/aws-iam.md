# aws iam

> Interagisce con Identity and Access Management (IAM), un servizio web per controllare in modo sicuro l'accesso ai servizi AWS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/iam/>.

- Elenca gli utenti:

`aws iam list-users`

- Elenca le policy:

`aws iam list-policies`

- Elenca i gruppi:

`aws iam list-groups`

- Ottieni gli utenti in un gruppo:

`aws iam get-group --group-name {{nome_gruppo}}`

- Descrivi una policy IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nome_policy}}`

- Elenca le chiavi di accesso:

`aws iam list-access-keys`

- Elenca le chiavi di accesso per un utente specifico:

`aws iam list-access-keys --user-name {{nome_utente}}`

- Visualizza l'aiuto:

`aws iam help`
