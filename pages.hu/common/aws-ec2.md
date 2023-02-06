# aws ec2

> CLI az AWS EC2-hez. Biztonságos és átméretezhető számítási kapacitást biztosít az AWS felhőben az alkalmazások gyorsabb fejlesztése és telepítése érdekében. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Egy adott példányra vonatkozó információk megjelenítése:

`aws ec2 describe-instances --instance-ids {{instance_id}}`

- Az összes példányra vonatkozó információk megjelenítése:

`aws ec2 describe-instances`

- Információk megjelenítése az összes EC2 kötetről:

`aws ec2 describe-volumes`

- EC2 kötet törlése:

`aws ec2 delete-volume --volume-id {{volume_id}}`

- Pillanatfelvétel készítése egy EC2 kötetből:

`aws ec2 create-snapshot --volume-id {{volume_id}}`

- Az elérhető AMI-k (Amazon Machine Images) listája:

`aws ec2 describe-images`

- Az összes elérhető EC2-parancs listájának megjelenítése:

`aws ec2 help`

- Súgó megjelenítése az adott EC2 alparancshoz:

`aws ec2 {{subcommand}} help`
