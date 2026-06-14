#կոկիկ

> Ներկայացրեք `linear undirected` ցանցային գրաֆիկի պատկերը `graphviz` ֆայլից:.
> Դասավորություններ՝ `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` և __IN_LINE_DE:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/doc/info/command.html>:.

- Ներկայացրեք PNG պատկեր ֆայլի անունով՝ հիմնված մուտքային ֆայլի անվան և ելքային ձևաչափի վրա (մեծատառ -O):

`neato -T {{png}} -O {{path/to/input.gv}}`

- Ներկայացրեք SVG պատկերը նշված ելքային ֆայլի անունով (փոքրատառ -o):

`neato -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Արտադրեք ելքը PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON կամ DOT ձևաչափերով.:

`neato -T {{format}} -O {{path/to/input.gv}}`

- Պատկերացրեք GIF պատկեր՝ օգտագործելով `stdin` և `stdout`:

`echo "{{graph {this -- that} }}" | neato -T {{gif}} > {{path/to/image.gif}}`

- Ցուցադրել օգնությունը.:

`neato -?`
