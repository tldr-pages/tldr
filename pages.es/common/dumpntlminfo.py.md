# DumpNTLMInfo.py

> Realiza una autenticación NTLM en un host remoto sin credenciales y extrae la información filtrada en el mensaje NTLMSSP.
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Extrae información NTLM del destino (SMB, puerto predeterminado 445):

`DumpNTLMInfo.py {{destino}}`

- Extrae información NTLM utilizando una IP específica:

`DumpNTLMInfo.py -target-ip {{ip_destino}} {{destino}}`

- Especifica un puerto personalizado:

`DumpNTLMInfo.py -port {{puerto}} {{destino}}`

- Extrae información NTLM utilizando el protocolo RPC (puerto predeterminado 135):

`DumpNTLMInfo.py -protocol RPC -port 135 {{destino}}`

- Activa la salida de depuración:

`DumpNTLMInfo.py -debug {{destino}}`
