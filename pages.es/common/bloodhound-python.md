# bloodhound-python

> Un ingestor Python para BloodHound, utilizado para enumerar las relaciones de Active Directory.
> Más información: <https://github.com/dirkjanm/BloodHound.py#usage>.

- Recopila todos los datos utilizando los métodos de recopilación predeterminados (incluye grupos, sesiones y fideicomisos):

`bloodhound-python --username {{nombre_de_usuario}} --password {{contraseña}} --domain {{dominio}}`

- Recopila datos utilizando la autenticación Kerberos sin requerir una contraseña en texto plano:

`bloodhound-python --collectionmethod {{Todos}} --kerberos --domain {{dominio}}`

- Se autentica utilizando hashes NTLM en lugar de una contraseña:

`bloodhound-python --collectionmethod {{Todos}} --username {{nombre_de_usuario}} --hashes {{LM:NTLM}} --domain {{dominio}}`

- Especifica un servidor de nombres personalizado para consultas DNS:

`bloodhound-python --collectionmethod {{Todos}}} --username {{nombre_de_usuario}} --password {{contraseña}} --domain {{dominio}} --nameserver {{nombre_de_servidor}}`

- Guarde los archivos de salida como un archivo ZIP comprimido:

`bloodhound-python --collectionmethod {{Todos}} --username {{nombre_de_usuario}} --password {{contraseña}} --domain {{dominio}} --zip`
