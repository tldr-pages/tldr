#ռեկտոր

> PHP 5.3+ կոդի թարմացման և վերամշակման ավտոմատացված գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/rectorphp/rector>:.

- Մշակել կոնկրետ գրացուցակ.:

`rector process {{path/to/directory}}`

- Մշակել գրացուցակը առանց փոփոխություններ կիրառելու (չոր գործարկում).:

`rector process {{path/to/directory}} --dry-run`

- Մշակել գրացուցակը և կիրառել կոդավորման ստանդարտներ.:

`rector process {{path/to/directory}} --with-style`

- Ցուցադրել առկա մակարդակների ցանկը.:

`rector levels`

- Մշակել գրացուցակ որոշակի մակարդակով.:

`rector process {{path/to/directory}} --level {{level_name}}`
