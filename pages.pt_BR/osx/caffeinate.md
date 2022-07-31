# caffeinate

> Evita que o macOS entre em suspensão (repouso).
> Mais informações: <https://ss64.com/osx/caffeinate.html>.

- Evitar a suspensão por uma hora (3600 segundos):

`caffeinate -u -t {{3600}}`

- Evitar a suspensão até que um comando seja concluído:

`caffeinate -s "{{comando}}"`

- Evitar a suspensão até que você digite Ctrl-C:

`caffeinate -i`
