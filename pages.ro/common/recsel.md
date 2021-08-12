# recsel

> Imprimarea înregistrărilor dintr-un recfile: o bază de date text simplu, editabilă de om.
> Mai multe informaţii: <https://www.gnu.org/software/recutils/manual/recutils.html>

- Extrage numele și câmpul de versiune:

`recsel -p name,version {{data.rec}}`

- Utilizați „~” pentru a se potrivi cu un șir cu o expresie regulată dată:

`recsel -e "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"`

- Utilizați un predicat pentru a se potrivi cu un nume și o versiune:

`recsel -e "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}`
