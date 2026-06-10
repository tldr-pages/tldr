# tlmgr առաջացնում

> Վերափոխեք կազմաձևման ֆայլերը տեղում պահված տեղեկություններից:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#generate>:.

- Վերափոխեք կազմաձևման ֆայլը, որը պահվում է որոշակի վայրում.:

`tlmgr generate --dest {{output_file}}`

- Վերափոխեք կազմաձևման ֆայլը, օգտագործելով տեղական կազմաձևման ֆայլը.:

`tlmgr generate --localcfg {{local_configuration_file}}`

- Գործարկեք անհրաժեշտ ծրագրերը կազմաձևման ֆայլերը վերակառուցելուց հետո.:

`tlmgr generate --rebuild-sys`
