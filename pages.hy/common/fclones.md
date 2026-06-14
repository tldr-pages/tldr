# fclones

> Արդյունավետ կրկնօրինակ ֆայլերի որոնիչ և հեռացնող:.
> Լրացուցիչ տեղեկություններ. <https://github.com/pkolaczk/fclones#usage>:.

- Որոնեք կրկնօրինակ ֆայլեր ընթացիկ գրացուցակում.:

`fclones group .`

- Որոնեք բազմաթիվ դիրեկտորիաներ կրկնօրինակ ֆայլերի համար և քեշեք արդյունքները.:

`fclones group --cache {{path/to/directory1 path/to/directory2 ...}}`

- Որոնեք միայն նշված գրացուցակը կրկնօրինակ ֆայլերի համար, բաց թողնելով ենթագրքեր և արդյունքները պահեք ֆայլի մեջ.:

`fclones group {{path/to/directory}} --depth 1 > {{path/to/file.txt}}`

- TXT ֆայլի կրկնօրինակ ֆայլերը տեղափոխեք մեկ այլ գրացուցակ.:

`fclones < {{path/to/file.txt}} move {{path/to/target_directory}}`

- Կատարեք TXT ֆայլի փափուկ հղումների չոր գործարկում՝ առանց իրականում կապելու.:

`fclones < {{path/to/file.txt}} link --soft --dry-run 2 > /dev/null`

- Ջնջեք նորագույն կրկնօրինակները ընթացիկ գրացուցակից՝ առանց դրանք ֆայլում պահելու.:

`fclones group . | fclones remove --priority newest`

- Նախամշակեք JPEG ֆայլերը ընթացիկ գրացուցակում՝ օգտագործելով արտաքին հրաման՝ հեռացնելով դրանց EXIF տվյալները՝ նախքան կրկնօրինակների համընկնումը:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
