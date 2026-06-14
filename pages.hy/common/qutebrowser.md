# qutebrowser

> Ստեղնաշարի վրա հիմնված, vim-ի նման զննարկիչ՝ հիմնված PyQt5-ի վրա:.
> Լրացուցիչ տեղեկություններ. <https://qutebrowser.org/doc/qutebrowser.1.html>:.

- Բացեք qutebrowser-ը նշված պահեստավորման գրացուցակով.:

`qutebrowser --basedir {{path/to/directory}}`

- Բացեք qutebrowser-ի օրինակ՝ ժամանակավոր կարգավորումներով.:

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- Վերականգնել qutebrowser օրինակի անվանված նիստը.:

`qutebrowser --restore {{session_name}}`

- Գործարկեք qutebrowser-ը՝ բացելով բոլոր URL-ները՝ օգտագործելով նշված մեթոդը.:

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- Բացեք qutebrowser-ը ժամանակավոր բազային գրացուցակով և տպեք տեղեկամատյանները `stdout` որպես JSON:

`qutebrowser --temp-basedir --json-logging`
