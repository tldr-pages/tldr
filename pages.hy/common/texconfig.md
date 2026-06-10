# texconfig

> Կարգավորեք TeX Live-ը կամ teTeX-ը:.
> Շատ դեպքերում փոխարինվում է `tlmgr`-ով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/texconfig>:.

- Ցուցադրել ընթացիկ TeX կոնֆիգուրացիան.:

`texconfig conf`

- Սահմանեք թղթի լռելյայն չափը աջակցվող ծրագրերի համար.:

`texconfig paper {{a4|letter|...}}`

- Սահմանեք PDFTeX-ի լռելյայն թղթի չափը.:

`texconfig pdftex paper {{a4|letter|...}}`

- Վերակառուցեք բոլոր TeX ձևաչափերը և տառատեսակների քարտեզները.:

`texconfig init`

- Վերակառուցեք հատուկ ձևաչափ.:

`texconfig init {{format}}`

- Թարմացրեք TeX ֆայլի անվան տվյալների բազան.:

`texconfig rehash`
