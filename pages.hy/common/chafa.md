#չաֆա

> Պատկերի տպում տերմինալում:.
> Տես նաև՝ `catimg`, `pixterm`:.
> Լրացուցիչ տեղեկություններ. <https://hpjansson.org/chafa/man/>:.

- Պատկերը ներկայացրեք անմիջապես տերմինալում.:

`chafa {{path/to/file}}`

- Ներկայացրեք պատկեր 24-բիթանոց գույնով.:

`chafa {{[-c|--colors]}} full {{path/to/file}}`

- Բարելավել պատկերների մատուցումը փոքր գունային գունապնակներով՝ օգտագործելով dithering:

`chafa {{[-c|--colors]}} 16 --dither ordered {{path/to/file}}`

- Պատկերացրեք պատկերը՝ դարձնելով այն պիքսելացված.:

`chafa --symbols vhalf {{path/to/file}}`

- Ներկայացրեք մոնոխրոմ պատկեր միայն բրայլյան նիշերով.:

`chafa {{[-c|--colors]}} none --symbols braille {{path/to/file}}`
