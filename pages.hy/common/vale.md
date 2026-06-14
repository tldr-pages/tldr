#վալե

> Ընդարձակվող ոճի ստուգիչ, որն աջակցում է նշագրման բազմաթիվ ձևաչափեր, ինչպիսիք են Markdown-ը և AsciiDoc-ը:.
> Լրացուցիչ տեղեկություններ. <https://vale.sh/docs/cli>:.

- Ստուգեք ֆայլի ոճը.:

`vale {{path/to/file}}`

- Ստուգեք ֆայլի ոճը նշված կոնֆիգուրացիայով.:

`vale --config='{{path/to/.vale.ini}}' {{path/to/file}}`

- Արդյունքները թողարկեք JSON ձևաչափով.:

`vale --output=JSON {{path/to/file}}`

- Ստուգեք ոճի խնդիրները հատուկ խստությամբ և ավելի բարձր.:

`vale --minAlertLevel={{suggestion|warning|error}} {{path/to/file}}`

- Ստուգեք ոճը `stdin`-ից՝ նշելով նշագրման ձևաչափը՝:

`cat {{file.md}} | vale --ext=.md`

- Թվարկեք ընթացիկ կոնֆիգուրացիան.:

`vale ls-config`
