# jq

> JSON պրոցեսոր, որն օգտագործում է տիրույթի հատուկ լեզու (DSL):.
> Լրացուցիչ տեղեկություններ. <https://jqlang.org/manual/>:.

- Կատարեք որոշակի արտահայտություն միայն `jq` երկուական տարբերակով (տպեք գունավոր և ձևաչափված JSON ելք).:

`jq '.' {{path/to/file.json}}`

- Կատարել կոնկրետ սցենար.:

`{{cat path/to/file.json}} | jq {{[-f|--from-file]}} {{path/to/script.jq}}`

- Անցնել հատուկ փաստարկներ.:

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- Ստեղծեք նոր JSON օբյեկտ մի քանի ֆայլերից հին JSON օբյեկտների միջոցով.:

`{{cat path/to/multiple_json_file_*.json}} | jq '{{{newKey1: .key1, newKey2: .key2.nestedKey, ...}}}'`

- Տպել հատուկ զանգվածի տարրեր.:

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- Տպել զանգված/օբյեկտի բոլոր արժեքները.:

`{{cat path/to/file.json}} | jq '.[]'`

- Տպեք առարկաները 2 պայմանի ֆիլտրով զանգվածում.:

`{{cat path/to/file.json}} | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- Ավելացնել/հեռացնել հատուկ ստեղներ.:

`{{cat path/to/file.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
