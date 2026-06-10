# lpadmin

> Կարգավորեք CUPS տպիչներն ու դասերը:.
> Տես նաև՝ `lpoptions`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-lpadmin.html>:.

- Սահմանեք լռելյայն տպիչը.:

`lpadmin -d {{printer}}`

- Ջնջել որոշակի տպիչ կամ դաս.:

`lpadmin -x {{printer|class}}`

- Ավելացնել տպիչ դասին.:

`lpadmin -p {{printer}} -c {{class}}`

- Հեռացրեք տպիչը դասից.:

`lpadmin -p {{printer}} -r {{class}}`
