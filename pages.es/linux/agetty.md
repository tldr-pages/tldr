# agetty

> Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`.
> Normalmente es invocado por `init`.
> Nota: la tasa de baudios es la velocidad de transferencia de datos entre una terminal y un dispositivo a través de una conexión serie.
> Más información: <https://manned.org/agetty>.

- Conecta `stdin` a un puerto (relativo a `/dev`) y especifica opcionalmente una tasa de baudios (cuyo valor predeterminado es 9600):

`agetty {{tty}} {{115200}}`

- Asume que `stdin` ya está conectado a una `tty` y establece un tiempo de espera para el inicio de sesión:

`agetty {{-t|--timeout}} {{tiempo_de_espera_en_segundos}} -`

- Asume que `tty` es de [8]-bits, sobreescribiendo la variable de entorno `TERM` establecida por `init`:

`agetty -8 - {{variable_term}}`

- Omite el inicio de sesión e invoca, como superusuario, otro programa de inicio de sesión en lugar de `/bin/login`:

`agetty {{-n|--skip-login}} {{-l|--login-program}} {{programa_de_inicio_de_sesión}} {{tty}}`

- Escribe el mensaje de inicio de sesión sin mostrar el contenido del archivo de pre-inicio de sesión (`/etc/issue` por predeterminado):

`agetty {{-i|--noissue}} -`

- Cambia el directorio raíz y escribe un host falso en el archivo `utmp`:

`agetty {{-r|--chroot}} {{/ruta/a/raíz_directorio}} {{-H|--host}} {{host_falso}} -`
