# կռունկ պատճեն

> Արդյունավետ կերպով պատճենեք հեռավոր պատկերը աղբյուրից թիրախ՝ պահպանելով ամփոփման արժեքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>:.

- Պատճենել պատկեր աղբյուրից թիրախ.:

`crane {{[cp|copy]}} {{source}} {{target}}`

- Պատճենել բոլոր պիտակները.:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-a|--all-tags]}}`

- Սահմանեք միաժամանակյա պատճենների առավելագույն քանակը, կանխադրված GOMAXPROCS:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-j|--jobs]}} {{int}}`

- Խուսափեք թիրախում առկա պիտակները վերագրելուց.:

`crane {{[cp|copy]}} {{source}} {{target}} {{[-n|--no-clobber]}}`

- Ցուցադրել օգնությունը.:

`crane {{[cp|copy]}} {{[-h|--help]}}`
