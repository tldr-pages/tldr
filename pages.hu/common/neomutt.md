# neomutt

> NeoMutt parancssori e-mail kliens. További információ: <https://neomutt.org>.

- Nyissa meg a megadott postafiókot:

`neomutt -f {{path/to/mailbox}}`

- Kezdjen el e-mailt írni, és adja meg a tárgyat és a `cc` címzettet:

`neomutt -s "{{subject}}" -c {{cc@example.com}} {{recipient@example.com}}`

- Küldjön e-mailt csatolt fájlokkal:

`neomutt -a {{path/to/file1 path/to/file2 ...}} -- {{recipient@example.com}}`

- Adjon meg egy fájlt, amelyet az üzenet törzseként csatolni kíván:

`neomutt -i {{path/to/file}} {{recipient@example.com}}`

- Az üzenet fejlécét és törzsét tartalmazó, RFC 5322 formátumú fájltervezet megadása:

`neomutt -H {{path/to/file}} {{recipient@example.com}}`
