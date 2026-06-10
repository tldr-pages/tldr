#ընտրություն

> PNG ֆայլի օպտիմալացման կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://optipng.sourceforge.net/optipng-7.9.1.man1.html>:.

- Սեղմեք PNG-ը լռելյայն կարգավորումներով.:

`optipng {{path/to/file.png}}`

- Սեղմեք PNG-ը լավագույն սեղմումով.:

`optipng -o {{7}} {{path/to/file.png}}`

- Սեղմեք PNG-ը ամենաարագ սեղմումով.:

`optipng -o {{0}} {{path/to/file.png}}`

- Սեղմեք PNG-ը և ավելացրեք միահյուսում.:

`optipng -i {{1}} {{path/to/file.png}}`

- Սեղմեք PNG-ը և պահպանեք բոլոր մետատվյալները (ներառյալ ֆայլի ժամանակային դրոշմանիշերը).:

`optipng -preserve {{path/to/file.png}}`

- Սեղմեք PNG-ը և հեռացրեք բոլոր մետատվյալները.:

`optipng -strip all {{path/to/file.png}}`
