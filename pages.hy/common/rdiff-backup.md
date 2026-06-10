# rdif-կրկնօրինակում

> Տեղական/հեռակառավարվող հայելի և լրացուցիչ պահուստավորման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://rdiff-backup.net/rdiff-backup.1.html>:.

- Կրկնօրինակեք `path/to/source`-ը `path/to/backup`-ում՝:

`rdiff-backup backup {{path/to/source}} {{path/to/backup}}`

- Ցուցակագրեք լրացուցիչ կրկնօրինակները պահեստում (տեղորոշման ուղի, տեղական կամ հեռավոր).:

`rdiff-backup list increments {{repository}}`

- Վերականգնել ամենավերջին կրկնօրինակից.:

`rdiff-backup restore {{path/to/backup}} {{path/to/destination}}`

- Վերականգնել պահուստավորված ֆայլերը այնպես, ինչպես 3 օր առաջ էին.:

`rdiff-backup restore --at 3D {{path/to/backup}} {{path/to/destination}}`
