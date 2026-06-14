# ncc

> Կազմել Node.js հավելվածը մեկ ֆայլի մեջ:.
> Աջակցում է TypeScript-ին, երկուական հավելումներին և դինամիկ պահանջներին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/vercel/ncc#usage>:.

- Միավորել Node.js հավելվածը՝:

`ncc build {{path/to/file.js}}`

- Միավորել և փոքրացնել Node.js հավելվածը.:

`ncc build {{[-m|--minify]}} {{path/to/file.js}}`

- Փաթեթավորեք և փոքրացրեք Node.js հավելվածը և ստեղծեք աղբյուրի քարտեզներ.:

`ncc build {{[-s|--source-map]}} {{path/to/file.js}}`

- Ինքնաբերաբար վերակազմավորել սկզբնաղբյուր ֆայլերի փոփոխությունները.:

`ncc build {{[-w|--watch]}} {{path/to/file.js}}`

- Միավորեք Node.js հավելվածը ժամանակավոր գրացուցակի մեջ և գործարկեք այն փորձարկման համար.:

`ncc run {{path/to/file.js}}`

- Մաքրել `ncc` քեշը.:

`ncc clean cache`
