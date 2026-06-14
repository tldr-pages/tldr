# microsoft-edge

> Ժամանակակից վեբ զննարկիչ, որը մշակվել է Microsoft-ի կողմից՝ հիմնված Google-ի կողմից մշակված Chromium վեբ բրաուզերի վրա:.
> Այս հրամանը հասանելի է որպես `msedge` Windows-ի համար:.
> Նշում․ `chromium`-ի լրացուցիչ արգումենտները կարող են օգտագործվել նաև Microsoft Edge-ը կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://microsoft.com/edge>:.

- Բացեք կոնկրետ URL կամ ֆայլ.:

`microsoft-edge {{https://example.com|path/to/file.html}}`

- Բացեք InPrivate ռեժիմում.:

`microsoft-edge --inprivate {{example.com}}`

- Բացեք նոր պատուհանում.:

`microsoft-edge --new-window {{example.com}}`

- Բացեք հավելվածի ռեժիմում (առանց գործիքագոտու, URL տողի, կոճակների և այլն):

`microsoft-edge --app={{https://example.com}}`

- Օգտագործեք վստահված սերվեր.:

`microsoft-edge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Բացեք անհատական պրոֆիլի գրացուցակով.:

`microsoft-edge --user-data-dir={{path/to/directory}}`

- Բացեք առանց CORS վավերացման (օգտակար API-ի փորձարկման համար).:

`microsoft-edge --user-data-dir={{path/to/directory}} --disable-web-security`

- Բացեք DevTools պատուհանով յուրաքանչյուր բացված ներդիրի համար.:

`microsoft-edge --auto-open-devtools-for-tabs`
