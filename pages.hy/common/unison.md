#միաձայն

> Երկկողմանի ֆայլերի համաժամացման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bcpierce00/unison>:.

- Համաժամացրեք երկու գրացուցակ (ստեղծում է գրանցամատյան առաջին անգամ, երբ այս երկու դիրեկտորիաները համաժամանակացվում են).:

`unison {{path/to/directory_1}} {{path/to/directory_2}}`

- Ավտոմատ կերպով ընդունեք (ոչ հակասական) կանխադրվածները.:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -auto`

- Անտեսեք որոշ ֆայլեր՝ օգտագործելով օրինաչափություն.:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}`

- Դիտեք փաստաթղթերը.:

`unison -doc {{topics}}`
