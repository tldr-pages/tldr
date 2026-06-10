#խառնել

> Ստեղծեք պատահական փոխարկումներ:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>:.

- Պատահականացրեք տողերի հերթականությունը ֆայլում և ստացեք արդյունքը.:

`shuf {{path/to/file}}`

- Արտադրեք միայն արդյունքի առաջին 5 գրառումները.:

`shuf {{[-n|--head-count]}} 5 {{path/to/file}}`

- Արդյունքը գրեք մեկ այլ ֆայլում.:

`shuf {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- Ստեղծեք 3 պատահական թիվ 1-10 միջակայքում (ներառյալ, թվերը կարող են կրկնվել).:

`shuf {{[-n|--head-count]}} 3 {{[-i|--input-range]}} 1-10 {{[-r|--repeat]}}`
