# aws sts

> Security Token Service (STS) permette di richiedere credenziali temporanee per utenti (IAM) o utenti federati.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Ottieni credenziali di sicurezza temporanee per accedere a risorse AWS specifiche:

`aws sts assume-role --role-arn {{arn_ruolo_aws}}`

- Ottieni un utente IAM o ruolo le cui credenziali sono utilizzate per chiamare l'operazione:

`aws sts get-caller-identity`
