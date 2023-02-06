# cotton

> Markdown teszt specifikáció futó. További információ: <https://github.com/chonla/cotton>.

- Egy adott alap-URL használata:

`cotton -u {{base_url}} {{path/to/file}}.md`

- A tanúsítványellenőrzés kikapcsolása (nem biztonságos mód):

`cotton -u {{base_url}} -i {{path/to/file}}.md`

- Állítsa le a futást, ha egy teszt sikertelen:

`cotton -u {{base_url}} -s {{path/to/file}}.md`
