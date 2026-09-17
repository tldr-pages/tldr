# aws ec2

> Gestisce istanze e volumi AWS EC2.
> AWS EC2 fornisce capacità di calcolo sicura e ridimensionabile nel cloud AWS per uno sviluppo e deployment più rapido delle applicazioni.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/ec2/>.

- Visualizza informazioni su un'istanza specifica:

`aws ec2 describe-instances --instance-ids {{id_istanza}}`

- Visualizza informazioni su tutte le istanze:

`aws ec2 describe-instances`

- Visualizza informazioni su tutti i volumi EC2:

`aws ec2 describe-volumes`

- Elimina un volume EC2:

`aws ec2 delete-volume --volume-id {{id_volume}}`

- Crea uno snapshot da un volume EC2:

`aws ec2 create-snapshot --volume-id {{id_volume}}`

- Elenca le AMI (Amazon Machine Images) disponibili:

`aws ec2 describe-images`

- Mostra l'elenco di tutti i comandi EC2 disponibili:

`aws ec2 help`

- Visualizza l'aiuto per un sottocomando EC2 specifico:

`aws ec2 {{sottocomando}} help`
