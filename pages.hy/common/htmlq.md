# htmlq

> Օգտագործեք CSS ընտրիչներ՝ HTML ֆայլերից բովանդակություն հանելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mgdm/htmlq#usage>:.

- Վերադարձրեք `card` դասի բոլոր տարրերը՝:

`cat {{path/to/file.html}} | htmlq '.card'`

- Ստացեք առաջին պարբերության տեքստի բովանդակությունը.:

`cat {{path/to/file.html}} | htmlq {{[-t|--text]}} 'p:first-of-type'`

- Գտեք էջի բոլոր հղումները.:

`cat {{path/to/file.html}} | htmlq {{[-a|--attribute]}} href 'a'`

- Հեռացրեք բոլոր պատկերները և SVG-ները էջից.:

`cat {{path/to/file.html}} | htmlq {{[-r|--remove-nodes]}} 'img' {{[-r|--remove-nodes]}} 'svg'`

- Գեղեցիկ տպեք և գրեք արդյունքը ֆայլում.:

`htmlq {{[-p|--pretty]}} {{[-f|--filename]}} {{path/to/input.html}} {{[-o|--output]}} {{path/to/output.html}}`
