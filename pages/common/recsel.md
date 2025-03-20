# recsel

> Print records from a recfile: a human-editable, plain text database.
> More information: <https://www.gnu.org/software/recutils/manual/recutils.html#Invoking-recsel>.

- Extract name and version field:

`recsel {{[-p|--print]}} name,version {{data.rec}}`

- Use "~" to match a string with a given regular expression:

`recsel {{[-e|--expression]}} "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"`

- Use a predicate to match a name and a version:

`recsel {{[-e|--expression]}} "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}`
