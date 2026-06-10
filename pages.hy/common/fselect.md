# ընտրեք

> Գտեք ֆայլեր SQL-ի նման հարցումներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jhspetersson/fselect/blob/master/docs/usage.md>:.

- Ընտրեք ամբողջական ուղին և չափը տվյալ գրացուցակի ժամանակավոր կամ կազմաձևման ֆայլերից.:

`fselect size, path from {{path/to/directory}} where name = '{{*.cfg}}' or name = '{{*.tmp}}'`

- Գտեք քառակուսի պատկերներ.:

`fselect path from {{path/to/directory}} where width = height`

- Գտեք հին դպրոցի ռեփ 320 կբ/վ MP3 ֆայլեր.:

`fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- Ընտրեք միայն առաջին 5 արդյունքները և թողարկեք որպես JSON:

`fselect size, path from {{path/to/directory}} limit {{5}} into json`

- Օգտագործեք SQL ագրեգատ գործառույթները գրացուցակում ֆայլերի նվազագույն, առավելագույն և միջին չափը հաշվարկելու համար.:

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"`
