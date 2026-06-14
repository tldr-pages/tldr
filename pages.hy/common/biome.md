#բիոմ

> Գործիքների շղթա՝ վեբ նախագծերի ձևաչափման, ծածկույթի և կոդի որակը ստուգելու համար:.
> Լրացուցիչ տեղեկություններ. <https://biomejs.dev/reference/cli/>:.

- Նախաձեռնեք նոր Biome կազմաձևման ֆայլ ընթացիկ գրացուցակում.:

`biome init`

- Ձևաչափեք ֆայլերը և վերագրեք դրանք տեղում.:

`biome format --write {{path/to/file_or_directory}}`

- Ստուգեք ձևաչափումը առանց փոփոխություններ կիրառելու.:

`biome format {{path/to/file_or_directory}}`

- Lint ֆայլեր և կիրառել անվտանգ շտկումներ.:

`biome lint --write {{path/to/file_or_directory}}`

- Գործարկեք ձևաչափը, ցողունը և ներմուծեք տեսակավորումը՝ կիրառելով անվտանգ շտկումներ.:

`biome check --write {{path/to/file_or_directory}}`

- Գործարկեք բոլոր ստուգումները CI ռեժիմով (ուղղումներ չեն կիրառվել, դուրս է գալիս սխալով, եթե խնդիրներ հայտնաբերվեն).:

`biome ci {{path/to/file_or_directory}}`

- Բացատրեք հատուկ lint կանոն.:

`biome explain {{rule_name}}`

- Ցուցադրման տարբերակը:

`biome {{[-V|--version]}}`
