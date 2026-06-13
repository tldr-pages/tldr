# sntp

> Un cliente para Simple Network Time Protocol.
> Más información: <https://keith.github.io/xcode-man-pages/sntp.1>.

- Consulta un servidor SNTP especificado y muestra la hora:

`sntp {{pool.ntp.org}}`

- Sincroniza el reloj del sistema con un servidor SNTP especificado:

`sudo sntp -S {{pool.ntp.org}}`

- Activa el registro de depuración:

`sntp -d {{pool.ntp.org}}`
