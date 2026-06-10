# տուփ

> Նկարել, հեռացնել և վերանորոգել ASCII արվեստի տուփերը:.
> Լրացուցիչ տեղեկություններ. <https://boxes.thomasjensen.com/boxes-man-1.html>:.

- Տողի շուրջ տուփ նկարիր.:

`echo "{{string}}" | boxes`

- Հեռացրեք տուփը տողից.:

`echo "{{string}}" | boxes {{[-r|--remove]}}`

- Նշեք տուփի դիզայնը.:

`echo "{{string}}" | boxes {{[-d|--design]}} {{parchment}}`

- Նշեք տուփի չափը (սյունակներում ըստ տողերի).:

`echo "{{string}}" | boxes {{[-s|--size]}} {{10}}x{{5}}`

- Հավասարեցրեք տուփի տեքստը [h]հորիզոնական ([l]ձախ, [c]enter կամ [r]աջ):

`echo "{{string}}" | boxes {{[-a|--align]}} h{{l|c|r}}`

- Հավասարեցրեք տուփի տեքստը [v] ուղղահայաց ([t]op, [c]enter կամ [b]ottom-ում):

`echo "{{string}}" | boxes {{[-a|--align]}} v{{t|c|b}}`

- [j]հիմնավորել տուփի տեքստը ([l]ձախ, [c]enter կամ [r]աջ):

`echo "{{string}}" | boxes {{[-a|--align]}} j{{l|c|r}}{{vt}}`
