# agetty

> Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`.
> Normalmente es invocado por `init`.
> Nota: la tasa de baudios es la velocidad de transferencia de datos entre una terminal y un dispositivo a través de una conexión serie.
> Más información: <https://manned.org/agetty>.

- Conecta `stdin` a un puerto (relativo a `/dev`) y especifica opcionalmente una tasa de baudios (por predeterminado 9600):

`agetty {{tty}} {{115200}}`

- Asume que `stdin` ya está conectado a una `tty` y establece un [t]iempo de espera para el inicio de sesión:

`agetty {{-t|--timeout}} {{tiempo_de_espera_en_segundos}} -`

- Asume que `tty` es de [8]-bits, anulando la variable de entorno `TERM` establecida por `init`:

`agetty -8 - {{term_var}}`

- Omite el inicio de sesión ([n]o inicio de sesión) e invoca, como superusuario, otro programa de inicio de sesión en lugar de `/bin/login`:

`agetty {{-n|--skip-login}} {{-l|--login-program}} {{login_program}} {{tty}}`

- No muestra el archivo de pre-inicio de sesión ([i]ssue) (`/etc/issue` por predeterminado) antes de escribir el mensaje de inicio de sesión:

`agetty {{-i|--noissue}} -`

- Cambia el directorio [r]aíz y escribe un falso [H]ost específico en el archivo `utmp`:

`agetty {{-r|--chroot}} {{/ruta/a/raíz_directorio}} {{-H|--host}} {{fake_host}} -`
