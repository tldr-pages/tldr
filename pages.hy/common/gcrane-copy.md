# gcrane պատճեն

> Արդյունավետ կերպով պատճենեք հեռավոր պատկերը աղբյուրից թիրախ՝ պահպանելով ամփոփման արժեքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>:.

- Պատճենել պատկեր աղբյուրից թիրախ.:

`gcrane {{[cp|copy]}} {{source}} {{target}}`

- Սահմանեք միաժամանակյա պատճենների առավելագույն քանակը, կանխադրված 20:

`gcrane copy {{source}} {{target}} {{[-j|--jobs]}} {{nr_of_copies}}`

- Արդյոք կրկնել պահեստների միջոցով.:

`gcrane copy {{source}} {{target}} {{[-r|--recursive]}}`

- Ցուցադրել օգնությունը.:

`gcrane copy {{[-h|--help]}}`
