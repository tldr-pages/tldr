#գրեքս

> Ստեղծեք `regex`s:.
> Լրացուցիչ տեղեկություններ. <https://github.com/pemistahl/grex#5-how-to-use>:.

- Ստեղծեք պարզ `regex`:

`grex {{string1 string2 ...}}`

- Ստեղծեք մեծատառերի անզգայուն `regex`:

`grex {{[-i|--ignore-case]}} {{string1 string2 ...}}`

- Թվերը փոխարինեք `\d`-ով.:

`grex {{[-d|--digits]}} {{string1 string2 ...}}`

- Unicode բառի նիշը փոխարինեք `\w`-ով:

`grex {{[-w|--words]}} {{string1 string2 ...}}`

- Փոխարինեք բացատները `\s`-ով.:

`grex {{[-s|--spaces]}} {{string1 string2 ...}}`

- Հայտնաբերել կրկնվող օրինաչափությունները մուտքագրման մեջ և կրճատել դրանք՝ օգտագործելով {min,max} քանակականները.:

`grex {{[-r|--repetitions]}} {{string1 string2 ...}}`

- Ստեղծեք `regex` թեստային դեպքեր (առանձնացված նոր տողով) ֆայլից.:

`grex {{[-f|--file]}} {{path/to/file}}`

- Մի ստեղծեք խարիսխներ և չգրանցող խմբեր.:

`grex --no-anchors {{[-g|--capture-groups]}} {{string1 string2 ...}}`
