# nxc smb

> Prueba y explota servidores SMB.
> Más información: <https://www.netexec.wiki/smb-protocol>.

- Busca credenciales de dominio válidas probando cada combinación en las listas especificadas de nombres de [u]suario y contraseñas:

`nxc smb {{192.168.178.2}} -u {{ruta/a/nombres_de_usuario.txt}} -p {{ruta/a/contraseñas.txt}}`

- Busca credenciales válidas para cuentas locales en lugar de cuentas de dominio:

`nxc smb {{192.168.178.2}} -u {{ruta/a/nombres_de_usuario.txt}} -p {{ruta/a/contraseñas.txt}} --local-auth`

- Enumera los recursos compartidos SMB y los derechos de acceso de los usuarios especificados en los hosts de destino:

`nxc smb {{192.168.178.0/24}} -u {{usuario}} -p {{contraseña}} --shares`

- Enumera las interfaces de red en los hosts de destino, realizando la autenticación mediante pass-the-hash:

`nxc smb {{192.168.178.30-45}} -u {{usuario}} -H {{NTLM_hash}} --interfaces`

- Analiza los hosts de destino en busca de vulnerabilidades frecuentes:

`nxc smb {{ruta/a/lista_objetivo.txt}} -u '' -p '' -M zerologon -M petitpotam`

- Intenta ejecutar un comando en los hosts de destino:

`nxc smb {{192.168.178.2}} -u {{usuario}} -p {{contraseña}} -x {{comando}}`
