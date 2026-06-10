# հոսքի հղում

> Արտահանեք հոսքերը տարբեր ծառայություններից և դրանք տեղափոխեք ընտրված տեսախցիկի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://streamlink.github.io/cli.html#command-line-usage>:.

- Փորձեք հանել հոսքերը նշված URL-ից, և եթե դա հաջող է, տպեք առկա հոսքերի ցանկը, որոնցից կարող եք ընտրել.:

`streamlink {{example.com/stream}}`

- Բացեք հոսք նշված որակով.:

`streamlink {{example.com/stream}} {{720p60}}`

- Ընտրեք ամենաբարձր կամ ամենացածր մատչելի որակը.:

`streamlink {{example.com/stream}} {{best|worst}}`

- Օգտագործեք հատուկ նվագարկիչ՝ հոսքի տվյալները փոխանցելու համար (VLC-ն օգտագործվում է լռելյայն, եթե գտնվել է).:

`streamlink {{[-p|--player]}} {{mpv}} {{example.com/stream}} {{best}}`

- Բաց թողնել որոշակի ժամանակ հոսքի սկզբից: Ուղիղ հեռարձակումների համար սա բացասական փոխհատուցում է հեռարձակման ավարտից (հետադարձ).:

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- Բաց թողնել ուղիղ հեռարձակման սկիզբը կամ որքան հնարավոր է հետ:

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- Նվագարկելու փոխարեն ֆայլի մեջ գրեք հոսքի տվյալները.:

`streamlink {{[-o|--output]}} {{path/to/file.ts}} {{example.com/stream}} {{best}}`

- Բացեք հոսքը նվագարկիչում, միևնույն ժամանակ այն գրելով ֆայլում.:

`streamlink {{[-r|--record]}} {{path/to/file.ts}} {{example.com/stream}} {{best}}`
