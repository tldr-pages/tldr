# getST.py

> Solicita un tique de servicio Kerberos (TGS).
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Solicita un tique de servicio para un SPN específico:

`getST.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}} -spn {{servicio}}/{{destino}}`

- Solicita un tique utilizando hash NTLM (pass-the-hash):

`getST.py -hashes {{LM_Hash}}:{{NT_Hash}} {{dominio}}/{{nombre_usuario}} -spn {{servicio}}/{{destino}}`

- Solicita un tique utilizando un archivo ccache de Kerberos existente:

`getST.py -no-pass -k {{dominio}}/{{nombre_usuario}} -spn {{servicio}}/{{destino}}`

- Suplanta a otro usuario mediante S4U2Self (requiere derechos de delegación):

`getST.py -k -impersonate {{target_user}} {{dominio}}/{{nombre_usuario}} -spn {{servicio}}/{{destino}}`

- Fuerza que el tique sea reenviable (Bronze Bit):

`getST.py -force-forwardable -k {{dominio}}/{{nombre_usuario}} -spn {{servicio}}/{{destino}}`
