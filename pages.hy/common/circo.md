# circo

> Ներկայացրեք `circular` ցանցային գրաֆիկի պատկերը `graphviz` ֆայլից:.
> Դասավորություններ՝ `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` և __IN_LINE_DE:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/doc/info/command.html>:.

- Ներկայացրեք PNG պատկեր ֆայլի անունով՝ հիմնված մուտքային ֆայլի անվան և ելքային ձևաչափի վրա (մեծատառ -O):

`circo -T {{png}} -O {{path/to/input.gv}}`

- Ներկայացրեք SVG պատկերը նշված ելքային ֆայլի անունով (փոքրատառ -o):

`circo -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Արտադրեք ելքը PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON կամ DOT ձևաչափերով.:

`circo -T {{format}} -O {{path/to/input.gv}}`

- Պատկերացրեք GIF պատկեր՝ օգտագործելով `stdin` և `stdout`:

`echo "{{digraph {this -> that} }}" | circo -T {{gif}} > {{path/to/image.gif}}`

- Ցուցադրել օգնությունը.:

`circo -?`
