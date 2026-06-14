# phpcbf

> Ուղղել phpc-ի կողմից հայտնաբերված խախտումները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/squizlabs/PHP_CodeSniffer>:.

- Ուղղեք խնդիրները նշված գրացուցակում (կանխադրված է PEAR ստանդարտին).:

`phpcbf {{path/to/directory}}`

- Ցուցադրել տեղադրված կոդավորման ստանդարտների ցանկը.:

`phpcbf -i`

- Նշեք կոդավորման ստանդարտ՝ վավերացնելու համար՝:

`phpcbf {{path/to/directory}} --standard {{standard}}`

- Նշեք ստորակետերով բաժանված ֆայլերի ընդարձակումները, որոնք կներառվեն հոտ քաշելիս.:

`phpcbf {{path/to/directory}} --extensions {{file_extension1,file_extension2,...}}`

- Ստորակետերով բաժանված ֆայլերի ցանկը, որը պետք է բեռնել նախքան մշակելը.:

`phpcbf {{path/to/directory}} --bootstrap {{path/to/file1,path/to/file2,...}}`

- Մի կրկնեք ենթագրքեր.:

`phpcbf {{path/to/directory}} -l`
