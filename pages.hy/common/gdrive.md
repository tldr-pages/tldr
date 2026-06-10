# gdrive

> Փոխազդել Google Drive-ի հետ:.
> Թղթապանակ/ֆայլի ID-ն կարելի է ձեռք բերել Google Drive-ի թղթապանակից կամ ID-ի URL-ից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/prasmussen/gdrive>:.

- Վերբեռնեք տեղական ուղի դեպի մայր թղթապանակ նշված ID-ով.:

`gdrive upload {{[-p|--parent]}} {{id}} {{path/to/file_or_folder}}`

- Ներբեռնեք ֆայլը կամ գրացուցակը ID-ով ընթացիկ գրացուցակում.:

`gdrive download {{id}}`

- Ներբեռնեք տվյալ տեղական ուղին իր ID-ով.:

`gdrive download --path {{path/to/folder}} {{id}}`

- Ստեղծեք ID-ի նոր վերանայում՝ օգտագործելով տվյալ ֆայլը կամ թղթապանակը.:

`gdrive update {{id}} {{path/to/file_or_folder}}`
