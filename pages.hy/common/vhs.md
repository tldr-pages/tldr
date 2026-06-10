# վհս

> Ստեղծեք տերմինալային GIF-ներ ժապավենային ֆայլից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/charmbracelet/vhs>:.

- Ստեղծեք ժապավենային ֆայլ (խմբագիր օգտագործելով ժապավենի ֆայլին հրամաններ ավելացրեք).:

`vhs new {{path/to/file.tape}}`

- Ձայնագրեք մուտքերը ժապավենի ֆայլում.:

`vhs record > {{path/to/file.tape}}`

- Գրանցեք մուտքերը ժապավենի ֆայլի մեջ՝ օգտագործելով հատուկ պատյան.:

`vhs record {{[-s|--shell]}} {{shell}} > {{path/to/file.tape}}`

- Դադարեցնել ձայնագրումը.:

`exit`

- Վավերացրեք ժապավենային ֆայլի շարահյուսությունը.:

`vhs validate {{path/to/file.tape}}`

- Ստեղծեք GIF ժապավենի ֆայլից.:

`vhs {{path/to/file.tape}}`

- Հրապարակեք GIF <https://vhs.charm.sh> և ստացեք համօգտագործվող URL.:

`vhs publish {{path/to/file.gif}}`
