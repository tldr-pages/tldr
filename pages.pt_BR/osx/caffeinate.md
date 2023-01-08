# caffeinate

> Evita que o macOS entre em suspensão (repouso).
> Mais informações: <https://ss64.com/osx/caffeinate.html>.

- Evita a suspensão por uma hora (3600 segundos):

`caffeinate -u -t {{3600}}`

- Evita a suspensão até que um comando seja concluído:

`caffeinate -s "{{comando}}"`

- Evita a suspensão até que você digite Ctrl-C:

`caffeinate -i`
