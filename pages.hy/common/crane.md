#կռունկ

> Կոնտեյների պատկերների կառավարման գործիք:.
> Որոշ ենթահրամաններ, ինչպիսիք են `pull`, `push`, `copy` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>:.

- Մուտք գործեք գրանցամատյան.:

`crane auth login {{registry}} {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}}`

- Գրանցամատյանում նշեք ռեպոները.:

`crane catalog {{registry}} --full-ref`

- Թվարկեք պիտակները պահեստում.:

`crane ls {{repository}} {{[-o|--omit-digest-tags]}}`

- Քաշեք հեռավոր պատկերները հղումով և պահեք դրանց բովանդակությունը տեղում.:

`crane pull {{image}} {{tarball}}`

- Տեղական պատկերի բովանդակությունը տեղափոխեք հեռավոր ռեեստր.:

`crane push {{path/to/directory_or_tarball}} {{image}}`

- Արդյունավետորեն նշեք հեռավոր պատկերը.:

`crane tag {{image}} {{tag}}`

- Արդյունավետ կերպով պատճենեք հեռավոր պատկերը` պահպանելով ամփոփման արժեքը.:

`crane {{[cp|copy]}} {{source}} {{destination}} {{[-a|--all-tags]}}`

- Ջնջել պատկերի հղումը իր ռեեստրից.:

`crane delete {{image}}`
