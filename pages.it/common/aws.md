# aws

> Il tool da linea di comando ufficiale per Amazon Web Services.
> Alcuni comandi aggiuntivi, come `aws s3`, hanno la propria documentazione.
> Maggiori informazioni: <https://aws.amazon.com/cli>.

- Lista tutti gli utenti IAM (Identity and Access Management):

`aws iam list-users`

- Lista tutte le instanze EC2 per una specifica regione:

`aws ec2 describe-instances --region {{us-east-1}}`

- Ricevi un messaggio da una specifica coda SQS:

`aws sqs receive-message --queue-url {{https://queue.amazonaws.com/546123/Test}}`

- Pubblica un messaggio SNS su uno specifico argomento:

`aws sns publish --topic-arn {{arn:aws:sns:us-east-1:54633:Agomento}} --message "Message"`

- Mostra la pagina di aiuto per uno specifico comando AWS:

`aws {{comando}} help`
