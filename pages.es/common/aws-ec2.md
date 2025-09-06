# aws ec2

> Interfaz de línea de comandos (CLI) para AWS EC2.
> Provee capacidad de computacion segura y redimensionable en la nube de AWS, permitiendo mayor velociddad en el desarrollo e implementación de aplicaciones.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Muestra información acerca de una instancia específica:

`aws ec2 describe-instances --instance-ids {{identificador_de_instancia}}`

- Muestra información sobre todas las instancias:

`aws ec2 describe-instances`

- Muestra información sobre todos los volúmenes EC2:

`aws ec2 describe-volumes`

- Elimina un volumen EC2:

`aws ec2 delete-volume --volume-id {{identificador_de_volumen}}`

- Crea una instantánea a partir de un volumen EC2:

`aws ec2 create-snapshot --volume-id {{identificador_de_volumen}}`

- Lista las imágenes de máquina de Amazon disponibles (AMI):

`aws ec2 describe-images`

- Lista todos los comandos EC2 disponibles:

`aws ec2 help`

- Muestra la ayuda para un comando EC2 específico:

`aws ec2 {{subcomando}} help`
