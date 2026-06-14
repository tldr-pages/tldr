# քրոմ

> Բաց կոդով վեբ զննարկիչը հիմնականում մշակվել և պահպանվում է Google-ի կողմից:.
> Նշում. Ձեզ անհրաժեշտ է փոխարինել `chromium` հրամանը ձեր ուզած վեբ դիտարկիչով, ինչպիսիք են `brave`, `google-chrome`, `opera` կամ `vivaldi`:.
> Լրացուցիչ տեղեկություններ. <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>:.

- Բացեք կոնկրետ URL կամ ֆայլ.:

`chromium {{https://example.com|path/to/file.html}}`

- Բացեք ինկոգնիտո ռեժիմում.:

`chromium --incognito {{example.com}}`

- Բացեք նոր պատուհանում.:

`chromium --new-window {{example.com}}`

- Բացեք հավելվածի ռեժիմում (առանց գործիքագոտու, URL տողի, կոճակների և այլն):

`chromium --app={{https://example.com}}`

- Օգտագործեք վստահված սերվեր.:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Բացեք անհատական պրոֆիլի գրացուցակով.:

`chromium --user-data-dir={{path/to/directory}}`

- Բացեք առանց CORS վավերացման (օգտակար API-ի փորձարկման համար).:

`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- Բացեք DevTools պատուհանով յուրաքանչյուր բացված ներդիրի համար.:

`chromium --auto-open-devtools-for-tabs`
