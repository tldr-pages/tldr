#ffe

> Արտահանեք դաշտերը հարթ տվյալների բազայի ֆայլից և գրեք այլ ձևաչափով:.
> Ներածումը մեկնաբանելու և ելքը ձևաչափելու համար պահանջվում է կազմաձևման ֆայլ:.
> Լրացուցիչ տեղեկություններ. <https://ff-extractor.sourceforge.net/ffe.html>:.

- Ցուցադրել բոլոր մուտքային տվյալները՝ օգտագործելով նշված տվյալների կազմաձևումը.:

`ffe {{[-c|--configuration]}} {{path/to/config.ffe}} {{path/to/input}}`

- Փոխակերպեք մուտքային ֆայլը ելքային ֆայլի նոր ձևաչափով.:

`ffe --output={{path/to/output}} {{[-c|--configuration]}} {{path/to/config.ffe}} {{path/to/input}}`

- Ընտրեք մուտքագրման կառուցվածքը և տպման ձևաչափը `~/.fferc` կազմաձևման ֆայլի սահմանումներից.:

`ffe {{[-s|--structure]}} {{structure}} {{[-p|--print]}} {{format}} {{path/to/input}}`

- Գրեք միայն ընտրված դաշտերը.:

`ffe {{[-f|--field-list]}} "{{FirstName,LastName,Age}}" {{[-c|--configuration]}} {{path/to/config.ffe}} {{path/to/input}}`

- Գրեք միայն այն գրառումները, որոնք համապատասխանում են արտահայտությանը.:

`ffe {{[-e|--expression]}} "{{LastName=Smith}}" {{[-c|--configuration]}} {{path/to/config.ffe}} {{path/to/input}}`

- Ցուցադրել օգնությունը.:

`ffe {{[-?|--help]}}`
