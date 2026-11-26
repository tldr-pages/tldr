# getTGT.py

> Solicita un Ticket Granting Ticket (TGT).
> Parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Solicita un TGT utilizando una contraseña:

`getTGT.py {{dominio}}/{{usuario}}:{{contraseña}}`

- Solicita un TGT utilizando hash NTLM:

`getTGT.py -hashes {{LM_Hash}}:{{NT_Hash}} {{dominio}}/{{usuario}}`

- Utiliza la autenticación Kerberos (desde un ccache existente, no se necesita contraseña):

`getTGT.py -k -no-pass {{dominio}}/{{usuario}}`

- Solicita un TGT utilizando una clave AES (128 ó 256 bits):

`getTGT.py -aesKey {{clave_aes}} {{dominio}}/{{usuario}}`

- Especifica una IP de controlador de dominio:

`getTGT.py -dc-ip {{ip_controlador_dominio}} {{dominio}}/{{usuario}}:{{contraseña}}`

- Solicita un tique de servicio directamente (AS-REQ) para un SPN específico:

`getTGT.py -service {{SPN}} {{dominio}}/{{usuario}}:{{contraseña}}`
