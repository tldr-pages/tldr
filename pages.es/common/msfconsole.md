# msfconsole

> Consola para el Metasploit Framework.
> Más información: <https://docs.rapid7.com/metasploit/msf-overview>.

- Inicia la consola:

`msfconsole`

- Lanza la consola [q]uietamente sin ningún mensaje:

`msfconsole --quiet`

- No habilita el soporte de bases de datos:

`msfconsole --no-database`

- Ejecuta los comandos de la consola (Nota: utiliza `;` para pasar varios comandos):

`msfconsole --execute-command "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- Muestra [v]ersión:

`msfconsole --version`
