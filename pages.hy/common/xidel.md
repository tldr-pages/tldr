# xidel

> Ներբեռնեք և հանեք տվյալները HTML/XML էջերից, ինչպես նաև JSON API-ներից:.
> Լրացուցիչ տեղեկություններ. <https://www.videlibri.de/xidel/>:.

- Տպեք բոլոր URL-ները, որոնք գտնվել են Google-ի որոնման միջոցով.:

`xidel {{https://www.google.com/search?q=test}} {{[-e|--extract]}} "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- Տպեք Google-ի որոնման միջոցով հայտնաբերված բոլոր էջերի անվանումը և ներբեռնեք դրանք.:

`xidel {{https://www.google.com/search?q=test}} {{[-f|--follow]}} "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" {{[-e|--extract]}} {{//title}} --download '{{{$host}/}}'`

- Հետևեք էջի բոլոր հղումներին և տպեք վերնագրերը XPath-ով.:

`xidel {{https://example.org}} {{[-f|--follow]}} {{//a}} {{[-e|--extract]}} {{//title}}`

- Հետևեք էջի բոլոր հղումներին և տպեք վերնագրերը՝ CSS ընտրիչներով.:

`xidel {{https://example.org}} {{[-f|--follow]}} "{{css('a')}}" --css {{title}}`

- Հետևեք էջի բոլոր հղումներին և տպեք վերնագրերը՝ օրինաչափությունների համապատասխանությամբ.:

`xidel {{https://example.org}} {{[-f|--follow]}} "{{<a>{.}</a>*}}" {{[-e|--extract]}} "{{<title>{.}</title>}}"`

- Կարդացեք օրինաչափությունը `example.xml`-ից (որը նաև կստուգի, թե արդյոք «ood» պարունակող տարրը կա, և հակառակ դեպքում չի հաջողվի):

`xidel {{path/to/example.xml}} {{[-e|--extract]}} "{{<x><foo>ood</foo><bar>{.}</bar></x>}}"`

- Տպեք Stack Overflow-ի բոլոր նորագույն հարցերը վերնագրով և URL-ով, օգտագործելով օրինաչափությունների համապատասխանությունը իրենց RSS հոսքում:

`xidel {{http://stackoverflow.com/feeds}} {{[-e|--extract]}} "{{<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+}}"`

- Ստուգեք չկարդացված Reddit փոստը, Webscraping-ը, CSS-ը, XPath-ը, JSONiq-ը համակցելով և ինքնաբերաբար ձևավորեք գնահատում.:

`xidel {{https://reddit.com}} {{[-f|--follow]}} "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" {{[-e|--extract]}} "{{css('#mail')/@title}}"`
