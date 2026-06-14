# կարևորում

> Արդյունք շարահյուսությամբ ընդգծված աղբյուրի կոդը տարբեր ձևաչափերով:.
> Լրացուցիչ տեղեկություններ. <http://andre-simon.de/doku/highlight/en/highlight.php>:.

- Ստեղծեք ամբողջական HTML փաստաթուղթ աղբյուրի կոդով ֆայլից.:

`highlight {{[-o|--out-format]}} {{html}} {{[-s|--style]}} {{theme_name}} {{[-S|--syntax]}} {{language}} {{path/to/source_code}}`

- Ստեղծեք HTML հատված, որը հարմար է ավելի մեծ փաստաթղթում ներառելու համար.:

`highlight {{[-o|--out-format]}} {{html}} {{[-f|--fragment]}} {{[-S|--syntax]}} {{language}} {{source_file}}`

- Ներդրեք CSS ոճը յուրաքանչյուր պիտակի մեջ.:

`highlight {{[-o|--out-format]}} {{html}} --inline-css {{[-S|--syntax]}} {{language}} {{source_file}}`

- Թվարկեք բոլոր աջակցվող լեզուները, թեմաները կամ հավելումները.:

`highlight --list-scripts {{langs|themes|plugins}}`

- Տպեք CSS ոճի թերթիկ թեմայի համար.:

`highlight {{[-o|--out-format]}} {{html}} --print-style {{[-s|--style]}} {{theme_name}} {{[-S|--syntax]}} {{language}} --stdout`
