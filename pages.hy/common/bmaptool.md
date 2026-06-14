# bmaptool

> Ստեղծեք կամ պատճենեք արգելափակման քարտեզները խելամտորեն (նախագծված են ավելի արագ, քան `cp` կամ `dd`):.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bmaptool>:.

- Արտադրեք բլոկ քարտեզի ֆայլ պատկերի ֆայլից.:

`bmaptool create {{[-o|--output]}} {{blockmap.bmap}} {{source.img}}`

- Պատճենեք պատկերի ֆայլը sdb-ում.:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- Պատճենեք սեղմված պատկերի ֆայլը sdb-ում.:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- Պատճենեք պատկերի ֆայլը sdb-ում՝ առանց բլոկ-քարտեզ օգտագործելու.:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`
