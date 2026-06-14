# xpdf

> Դյուրակիր փաստաթղթի ձևաչափի (PDF) ֆայլերի դիտում:.
> Լրացուցիչ տեղեկություններ. <https://www.xpdfreader.com/xpdf-man.html>:.

- Բացեք PDF ֆայլ.:

`xpdf {{path/to/file.pdf}}`

- Բացեք որոշակի էջ PDF ֆայլում.:

`xpdf {{path/to/file.pdf}} :{{page_number}}`

- Բացեք սեղմված PDF ֆայլ.:

`xpdf {{path/to/file.pdf.tar}}`

- Բացեք PDF ֆայլ լիաէկրան ռեժիմով.:

`xpdf -fullscreen {{path/to/file.pdf}}`

- Նշեք սկզբնական խոշորացումը.:

`xpdf -z {{75}}% {{path/to/file.pdf}}`

- Նշեք սկզբնական խոշորացումը էջի լայնությամբ կամ ամբողջ էջի վրա.:

`xpdf -z {{page|width}} {{path/to/file.pdf}}`
