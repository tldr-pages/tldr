# terminal-notifier

> Envía notificaciones de usuario en macOS.
> Más información: <https://github.com/julienXX/terminal-notifier>.

- Envía una notificación (sólo se necesita el mensaje):

`terminal-notifier -group {{tldr-info}} -title {{TLDR}} -message '{{TLDR mola}}'`

- Muestra datos transmitidos con un sonido:

`echo '{{Datos de mensajes transmitidos!}}' | terminal-notifier -sound {{default}}`

- Abre una URL al hacer clic en la notificación:

`terminal-notifier -message '{{Comprueba tus acciones de Apple!}}' -open '{{http://finance.yahoo.com/q?s=AAPL}}'`

- Abre una aplicación al hacer clic en la notificación:

`terminal-notifier -message '{{Importados 42 contactos.}}'  -activate {{com.apple.AddressBook}}`
