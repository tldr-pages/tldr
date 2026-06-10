#դեմիքս

> Deezloader Remix-ի մոխիրներից կառուցված «deezer» ներբեռնող անծանոթ գրադարան:.
> Այն կարող է օգտագործվել որպես ինքնուրույն CLI հավելված կամ ներդրվել UI-ում՝ օգտագործելով API:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/RemixDev/deemix-py>:.

- Ներբեռնեք երգ կամ երգացանկ.:

`deemix {{https://www.deezer.com/us/track/00000000}}`

- Ներբեռնեք երգը / երգացանկը հատուկ բիթային արագությամբ.:

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- Ներբեռնեք կոնկրետ ճանապարհով.:

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- Ստեղծեք շարժական deemix կազմաձևման ֆայլ ընթացիկ գրացուցակում.:

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`
