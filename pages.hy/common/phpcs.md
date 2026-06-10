# phpcs

> Թոքենիզացրեք PHP, JavaScript և CSS ֆայլերը՝ կոդավորման սահմանված ստանդարտների խախտումները հայտնաբերելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/squizlabs/PHP_CodeSniffer>:.

- Հոտեք նշված գրացուցակը խնդիրների համար (կանխադրված է PEAR ստանդարտին).:

`phpcs {{path/to/directory}}`

- Ցուցադրել տեղադրված կոդավորման ստանդարտների ցանկը.:

`phpcs -i`

- Նշեք կոդավորման ստանդարտ՝ վավերացնելու համար՝:

`phpcs {{path/to/directory}} --standard {{standard}}`

- Նշեք ստորակետերով բաժանված ֆայլերի ընդարձակումները, որոնք կներառվեն հոտ քաշելիս.:

`phpcs {{path/to/directory}} --extensions {{file_extension1,file_extension2,...}}`

- Նշեք ելքային հաշվետվության ձևաչափը (օրինակ՝ `full`, `xml`, `json`, `summary`):

`phpcs {{path/to/directory}} --report {{format}}`

- Սահմանեք կազմաձևման փոփոխականները, որոնք պետք է օգտագործվեն գործընթացի ընթացքում.:

`phpcs {{path/to/directory}} --config-set {{key}} {{value}}`

- Ստորակետերով բաժանված ֆայլերի ցանկը, որը պետք է բեռնել նախքան մշակելը.:

`phpcs {{path/to/directory}} --bootstrap {{path/to/file1,path/to/file2,...}}`

- Մի կրկնեք ենթագրքեր.:

`phpcs {{path/to/directory}} -l`
