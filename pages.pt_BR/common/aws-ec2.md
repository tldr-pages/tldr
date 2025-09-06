# aws ec2

> Inteface de linha de comando para o AWS EC2.
> Provê capacidade computacional segura e flexível na nuvem da AWS para proporcionar um desenvolvimento e subida para produção de aplicações rapidamente.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Exibe informações sobre uma insntância específica:

`aws ec2 describe-instances --instance-ids {{id_da_instância}}`

- Exibe informações sobre todas as instâncias:

`aws ec2 describe-instances`

- Exibe informações sobre todos os volumes EC2:

`aws ec2 describe-volumes`

- Deleta um volume EC2:

`aws ec2 delete-volume --volume-id {{id_do_volume}}`

- Cria um snapshot de um volume EC2:

`aws ec2 create-snapshot --volume-id {{id_do_volume}}`

- Lista as AMIs (Imagem de Máquina da Amazon) disponíveis:

`aws ec2 describe-images`

- Lista todos os comandos EC2 disponíveis:

`aws ec2 help`

- Exibe ajuda específica para um subcomando da EC2:

`aws ec2 {{subcomando}} help`
