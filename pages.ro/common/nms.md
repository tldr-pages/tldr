# nms

> Instrument de linie de comandă care recreează faimosul efect de decriptare a datelor văzut în filmul 1992 Sneakers de la stdin.
> Mai multe informaţii: <https://github.com/bartobri/no-more-secrets>

- Decriptarea textului după o apăsare de tastă:

`echo "{{Hello, World!}}" | nms`

- Decriptează ieșirea imediat, fără a aștepta o apăsare de tastă:

`{{ls -la}} | nms -a`

- Decripta continutul unui fisier, cu o culoare de iesire personalizata:

`cat {{path/to/file}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- Ștergeți ecranul înainte de decriptare:

`{{command}} | nms -a -c`
