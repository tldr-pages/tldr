#նամ

> Netwide Assembler-ը, շարժական 80x86 չափսի հավաքիչ:.
> Լրացուցիչ տեղեկություններ. <https://www.nasm.us/xdoc/3.01/html/nasm02.html>:.

- Հավաքեք `source.asm`-ը երկուական ֆայլի մեջ `source`՝ (կանխադրված) չմշակված երկուական ձևաչափով՝:

`nasm {{source.asm}}`

- Հավաքեք `source.asm` երկուական ֆայլ `output_file`՝ նշված ձևաչափով.:

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- Ցուցակեք վավեր ելքային ձևաչափերը (հիմնական nasm օգնության հետ միասին).:

`nasm -hf`

- Հավաքեք և ստեղծեք հավաքման ցուցակման ֆայլ.:

`nasm -l {{list_file}} {{source.asm}}`

- Ավելացրեք գրացուցակ (պետք է գրվի վերջավոր կտրվածքով) ներառել ֆայլի որոնման ճանապարհին, նախքան հավաքելը.:

`nasm -i {{path/to/include_directory}}/ {{source.asm}}`
