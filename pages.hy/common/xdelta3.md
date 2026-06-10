# xdelta3

> Երկուական ֆայլերի դելտա սեղմման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jmacd/xdelta/blob/wiki/CommandLineSyntax.md>:.

- Ստեղծեք կարկատել ([e]կոդ)՝ հիմնված [s]source ֆայլի վրա.:

`xdelta3 -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`

- Կիրառեք կարկատել ([d]ecompress) [s]source ֆայլի վրա.:

`xdelta3 -d -s {{path/to/old_file}} {{path/to/patch_file}} {{path/to/new_file}}`

- Ստեղծեք կարկատել հատուկ սեղմման մակարդակով.:

`xdelta3 -{{0..9}} -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`
