#քրոմա

> Ընդհանուր նշանակության շարահյուսական ընդգծող:.
> `--lexer` տարբերակը սովորաբար ավելորդ է, քանի որ այն ավտոմատ կերպով որոշվելու է ֆայլի ընդլայնման հիման վրա:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/chroma>:.

- Նշեք Python lexer-ով ֆայլի սկզբնական կոդը և թողարկեք `stdout`:

`chroma {{[-l|--lexer]}} {{python}} {{path/to/source_file.py}}`

- Ընդգծեք աղբյուրի կոդը Go lexer-ով ֆայլից և դուրս բերեք HTML ֆայլ.:

`chroma {{[-l|--lexer]}} {{go}} {{[-f|--formatter]}} {{html}} {{path/to/source_file.go}} > {{path/to/target_file.html}}`

- Ընդգծեք `stdin`-ի սկզբնական կոդը C++ lexer-ով և թողարկեք SVG ֆայլ՝ օգտագործելով Monokai ոճը:

`{{command}} | chroma {{[-l|--lexer]}} {{c++}} {{[-f|--formatter]}} {{svg}} {{[-s|--style]}} {{monokai}} > {{path/to/target_file.svg}}`

- Ցուցակեք առկա lexers, ոճերը և ձևաչափերը.:

`chroma --list`
