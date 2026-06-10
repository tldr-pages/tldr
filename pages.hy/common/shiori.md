#շիորի

> Պարզ էջանիշերի կառավարիչ, որը ստեղծվել է Go-ով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/go-shiori/shiori/blob/master/docs/Usage.md>:.

- Ներմուծեք էջանիշներ HTML Netscape էջանիշերի ձևաչափի ֆայլից.:

`shiori import {{path/to/bookmarks.html}}`

- Պահպանեք նշված URL-ը որպես էջանիշ.:

`shiori add {{url}}`

- Թվարկեք պահպանված էջանիշները.:

`shiori print`

- Բացեք պահպանված էջանիշը դիտարկիչում.:

`shiori open {{bookmark_id}}`

- Սկսեք վեբ ինտերֆեյսը 8181 նավահանգստում էջանիշները կառավարելու համար.:

`shiori serve --port {{8181}}`
