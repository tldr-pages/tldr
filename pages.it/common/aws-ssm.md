# aws ssm

> Interagisce in modo sicuro con le risorse AWS e le gestisce.
> Nota: le sessioni interattive richiedono che il Session Manager plugin sia installato.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/ssm/>.

- Esegue comandi sulle istanze:

`aws ssm send-command --instance-ids {{id_istanza1 id_istanza2 ...}} --document-name "AWS-RunShellScript" --parameters 'commands=["{{comando}}"]'`

- Controlla le esecuzioni dei comandi su un'istanza:

`aws ssm list-command-invocations --instance-id "{{id_istanza}}"`

- Controlla l'output di un comando specifico:

`aws ssm list-command-invocations --command-id "{{id_comando}}" --details`

- Avvia una sessione interattiva con un'istanza:

`aws ssm start-session --target "{{id_istanza}}"`

- Avvia una sessione di port forwarding verso un host remoto:

`aws ssm start-session --target "{{id_istanza}}" --document-name "AWS-StartPortForwardingSessionToRemoteHost" --parameters '{"portNumber":["{{porta_remota}}"],"localPortNumber":["{{porta_locale}}"]}'`
