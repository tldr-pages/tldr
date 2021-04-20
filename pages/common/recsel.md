# recsel

> Print records from a recfile: a human-editable, plain text database.
> More information: <https://www.gnu.org/software/recutils/manual/recutils.html>.

- Extract name and version field:

`recsel -p name,version {{data.rec}}`

- Use "~" to match a string with a given regular expression:

`recsel -e "{{field_name}} ~ '{{pattern_regex}}' {{data.rec}}"`

- Use a predicate to match a name and a version:

`recsel -e "name ~ '{{pattern_regex}}' && version ~ '{{pattern_regex}}'" {{data.rec}}`
