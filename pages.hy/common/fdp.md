# fdp

> Ներկայացրեք `force-directed` ցանցային գրաֆիկի պատկերը `graphviz` ֆայլից:.
> Դասավորություններ՝ `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` և __INLINE_CO:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/doc/info/command.html>:.

- Ներկայացրեք PNG պատկեր ֆայլի անունով՝ հիմնված մուտքային ֆայլի անվան և ելքային ձևաչափի վրա (մեծատառ -O):

`fdp -T png -O {{path/to/input.gv}}`

- Ներկայացրեք SVG պատկերը նշված ելքային ֆայլի անունով (փոքրատառ -o):

`fdp -T svg -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Արտադրեք արդյունքը հատուկ ձևաչափով.:

`fdp -T {{ps|pdf|svg|fig|png|gif|jpg|json|dot}} -O {{path/to/input.gv}}`

- Պատկերացրեք `gif` պատկերը՝ օգտագործելով `stdin` և `stdout`:

`echo "{{digraph {this -> that} }}" | fdp -T gif > {{path/to/image.gif}}`

- Ցուցադրել օգնությունը.:

`fdp -?`
