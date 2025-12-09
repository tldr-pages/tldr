# aws route53

> CLI para AWS Route53 - Route 53 es un servicio web de Sistema de Nombres de Dominio (DNS) altamente disponible y escalable.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- Lista todas las zonas alojadas, privadas y públicas:

`aws route53 list-hosted-zones`

- Muestra todos los registros de una zona:

`aws route53 list-resource-record-sets --hosted-zone-id {{identificador_de_zona}}`

- Crea una nueva zona pública utilizando un identificador de solicitud para reintentar la operación de forma segura:

`aws route53 create-hosted-zone --name {{nombre}} --caller-reference {{identificador_de_solicitud}}`

- Elimina una zona (si la zona tiene registros SOA y NS no predeterminados, el comando fallará):

`aws route53 delete-hosted-zone --id {{identificador_de_zona}}`

- Prueba la resolución DNS por parte de los servidores de Amazon de una zona determinada:

`aws route53 test-dns-answer --hosted-zone-id {{identificador_de_zona}} --record-name {{nombre}} --record-type {{tipo}}`
