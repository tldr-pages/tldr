# expr

> Evalueer expressies en manipuleer string.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- Krijg de lengte van een specifieke string:

`expr length "{{string}}"`

- Krijg de substring van een string met een specifieke lengte:

`expr substr "{{string}}" {{van}} {{lengte}}`

- Vergelijk een specifieke substring met een verankerd patroon:

`expr match "{{string}}" '{{patroon}}'`

- Verkrijg de eerste karakterpositie van een specifieke set in een tekenreeks:

`expr index "{{string}}" "{{karakters}}"`

- Bereken een specifieke mathematische expressie:

`expr {{expressie1}} {{+|-|*|/|%}} {{expressie2}}`

- Bekijk de eerste expressie als de waarde niet nul is en niet null, anders de tweede:

`expr {{expressie1}} \| {{expressie2}}`

- Bekijk de eerste expressie als beide expressies niet nul zijn en niet null, anders 0:

`expr {{expressie1}} \& {{expressie2}}`
