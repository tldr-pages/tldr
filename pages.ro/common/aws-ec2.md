# aws ec2

> CLI pentru AWS EC2.
> Oferă o capacitate de calcul sigură şi redimensionabilă în cloud AWS pentru a permite dezvoltarea şi implementarea mai rapidă a aplicaţiilor.
> Mai multe informaţii: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>

- Afișează lista tuturor comenzilor EC2 disponibile:

`aws ec2 help`

- Arată ajutor pentru subcomanda EC2 specifică:

`aws ec2 {{subcommand}} help`

- Afișați informații despre o anumită instanță:

`aws ec2 describe-instances --instance-ids {{instance_id}}`

- Afișează informații despre toate instanțele:

`aws ec2 describe-instances`

- Afișează informații despre toate volumele EC2:

`aws ec2 describe-volumes`

- Ștergeți un volum EC2:

`aws ec2 delete-volume --volume-id {{volume_id}}`

- Creați un instantaneu dintr-un volum EC2:

`aws ec2 create-snapshot --volume-id {{volume_id}}`

- Lista AMI disponibile (Amazon Machine Images):

`aws ec2 describe-images`
