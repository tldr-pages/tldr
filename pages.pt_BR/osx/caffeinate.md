# caffeinate

> Evita que o macOS entre em suspensão (repouso).
> Mais informações: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Evita a suspensão por uma hora (3600 segundos):

`caffeinate -u -t {{3600}}`

- Evita a suspensão até que um comando seja concluído:

`caffeinate -s "{{comando}}"`

- Evita a suspensão até que você digite Ctrl-C:

`caffeinate -i`
