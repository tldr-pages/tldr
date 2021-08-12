# httping

> Măsurați latența și debitul unui server web.
> Mai multe informaţii: <https://manned.org/httping>

- Ping URL-ul specificat:

`httping -g {{url}}`

- Ping serverul web pe `gazd` si `port`:

`httping -h {{host}} -p {{port}}`

- Ping serverul web pe `gazd` folosind o conexiune TLS:

`httping -l -g https://{{host}}`

- Ping serverul web pe `gazd` folosind autentificarea de bază HTTP:

`httping -g http://{{host}} -U {{username}} -P {{password}}`
