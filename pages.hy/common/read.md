#կարդալ

> Shell-ը ներկառուցված է `stdin`-ից տվյալների առբերման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-read>:.

- Պահպանեք ձեր մուտքագրած տվյալները ստեղնաշարից.:

`read {{variable}}`

- Պահպանեք ձեր մուտքագրած հաջորդ տողերից յուրաքանչյուրը որպես զանգվածի արժեքներ.:

`read -a {{array}}`

- Նշեք ընթերցվող առավելագույն նիշերի քանակը.:

`read -n {{character_count}} {{variable}}`

- Բազմաթիվ արժեքներ վերագրեք մի քանի փոփոխականներին.:

`read <<< "{{The surname is Bond}}" {{_ variable1 _ variable2}}`

- Թույլ մի տվեք, որ հետադարձ կտրվածքը (`\`) հանդես գա որպես փախուստի նշան.:

`read -r {{variable}}`

- Ցուցադրել հուշում մուտքագրումից առաջ.:

`read -p "{{Enter your input here: }}" {{variable}}`

- Մի արձագանքեք մուտքագրված նիշերին (լուռ ռեժիմ).:

`read -s {{variable}}`

- Կարդացեք `stdin`-ը և կատարեք գործողություն յուրաքանչյուր տողում.:

`cat {{/dev/stdin|path/to/file|...}} | while read line; do {{echo|ls|rm|...}} "$line"; done`
