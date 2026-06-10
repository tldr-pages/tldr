# fiascotopnm

> Վերափոխեք սեղմված FIASCO ֆայլը PNM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/fiascotopnm.html>:.

- Սեղմված FIASCO ֆայլը փոխարկեք PNM ֆայլի կամ մի քանի PNM ֆայլերի վիդեո հոսքերի դեպքում.:

`fiascotopnm {{path/to/file.fiasco}} {{[-o|--output]}} {{output_file_basename}}`

- Օգտագործեք արագ ապակոմպրեսիա, ինչը հանգեցնում է ելքային ֆայլ(ների) որակի մի փոքր նվազմանը.:

`fiascotopnm {{[-z|--fast]}} {{path/to/file.fiasco}} {{[-o|--output]}} {{output_file_basename}}`

- Բեռնել ընտրանքները, որոնք պետք է օգտագործվեն նշված կազմաձևման ֆայլից.:

`fiascotopnm {{[-f|--config]}} {{path/to/fiascorc}} {{path/to/file.fiasco}} {{[-o|--output]}} {{output_file_basename}}`

- Խոշորացրեք ապասեղմված պատկեր(ներ)ը 2^n գործակցով.:

`fiascotopnm {{[-m|--magnify]}} {{n}} {{path/to/file.fiasco}} {{[-o|--output]}} {{output_file_basename}}`

- Հարթեցրեք ապասեղմված պատկերը նշված չափով.:

`fiascotopnm {{[-s|--smoothing]}} {{n}} {{path/to/file.fiasco}} {{[-o|--output]}} {{output_file_basename}}`
