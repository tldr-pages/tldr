# terminal-notifier

> Envia notificaciones de usuario en macOS.
> Más información: <https://github.com/julienXX/terminal-notifier>.

- Envia una notificación (sólo se requiere el mensaje):

`terminal-notifier -group {{tldr-info}} -title {{TLDR}} -mensaje '{{TLDR mola}}'`

- Muestra datos canalizados con un sonido:

`echo '{{¡Datos de mensajes canalizados!}}'' | terminal-notifier -sound {{default}}`

- Abre una URL al hacer clic en la notificación:

`terminal-notifier -message '{{¡Comprueba tus acciones de Apple!}}' -open '{{! -open '{{http://finance.yahoo.com/q?s=AAPL}}'`

- Abre una aplicación al hacer clic en la notificación:

`terminal-notifier -message '{{Se importaron 42 contactos.}}'  -activate {{com.apple.AddressBook}}`
