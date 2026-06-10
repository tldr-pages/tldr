# տառասխալ

> Գտեք և ուղղեք սկզբնաղբյուրում առկա ուղղագրական սխալները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/crate-ci/typos/blob/master/docs/reference.md>:.

- Ստուգեք ֆայլը կամ գրացուցակը ուղղագրական սխալների համար.:

`typos {{path/to/file_or_directory}}`

- Ֆայլի կամ գրացուցակի մեջ ավտոմատ կերպով ուղղել տառասխալները.:

`typos {{[-w|--write-changes]}} {{path/to/file_or_directory}}`

- Նախադիտեք փոփոխությունները նախքան դրանք կիրառելը.:

`typos --diff {{path/to/file_or_directory}}`

- Ստուգեք ֆայլը կամ գրացուցակը, ներառյալ թաքնված ֆայլերը և գրացուցակները.:

`typos --hidden {{path/to/file_or_directory}}`

- Ստուգեք ֆայլը կամ գրացուցակը, անտեսելով ֆայլերը, որոնք համապատասխանում են որոշակի գլոբուսի օրինակին.:

`typos --exclude {{pattern}} {{path/to/file_or_directory}}`

- Գրեք ընթացիկ կոնֆիգուրացիան որոշակի ֆայլում.:

`typos --dump-config {{path/to/typos.toml}}`

- Թվարկեք բոլոր աջակցվող ֆայլերի տեսակները.:

`typos --type-list`

- Ցույց տալ ուղղագրական սխալները որոշակի ելքային ձևաչափով (կանխադրված է `long`):

`typos --format {{brief|long|json|...}} {{path/to/file_or_directory}}`
