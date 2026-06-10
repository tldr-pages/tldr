# մեկ

> Սերիալացրեք պահեստը կամ գրացուցակը LLM-ի համար հարմար մեկ ֆայլի մեջ (արագ Rust-ի վրա հիմնված repomapper):.
> Լրացուցիչ տեղեկություններ. <https://github.com/bodo-run/yek#usage>:.

- Սերիալացրեք ընթացիկ գրացուցակը և ելքը գրեք ժամանակավոր ֆայլում (տպման ուղի).:

`yek`

- Սերիականացնել հատուկ դիրեկտորիաներ և ելք գրել գրացուցակում.:

`yek {{path/to/directory1 path/to/directory2 ...}} --output-dir {{path/to/output_directory}}`

- Մշակեք բազմաթիվ ֆայլեր կամ օգտագործեք գլոբային նախշեր (մեջբերեք գլոբուսները՝ կեղևի ընդլայնումից խուսափելու համար).:

`yek "{{path/to/directory/**/*.rs}}" "{{path/to/directory/**/*.md}}"`

- Նշանների վրա հիմնված ելքային չափը փակեք մինչև 128 հազար նշան.:

`yek {{path/to/directory}} --tokens 128k`

- Ծածկեք բայթի վրա հիմնված առավելագույն թողարկման չափը և սահմանեք ելքային ֆայլի հստակ անուն.:

`yek {{path/to/directory}} --max-size {{100KB}} --output-name {{yek-output.txt}}`

- Stream JSON ելք.:

`yek {{path/to/directory}} --json`

- Արդյունքում ներառեք գրացուցակի ծառի վերնագիր.:

`yek {{path/to/directory}} --tree-header`
