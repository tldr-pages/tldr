# mutt

> Parancssori e-mail kliens. További információ: <http://mutt.org>.

- Nyissa meg a megadott postafiókot:

`mutt -f {{mailbox}}`

- Küldjön e-mailt, és adja meg a tárgyat és a cc címzettet:

`mutt -s {{subject}} -c {{cc@example.com}} {{recipient@example.com}}`

- E-mail küldése csatolt fájlokkal:

`mutt -a {{file1}} {{file2}} -- {{recipient@example.com}}`

- Adjon meg egy fájlt, amelyet az üzenet törzseként csatolni kíván:

`mutt -i {{path/to/file}} {{recipient@example.com}}`

- Az üzenet fejlécét és törzsét tartalmazó, RFC 5322 formátumú fájltervezet megadása:

`mutt -H {{path/to/file}} {{recipient@example.com}}`
