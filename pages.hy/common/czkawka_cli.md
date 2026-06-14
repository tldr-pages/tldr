# czkawka_cli

> Գտեք կրկնօրինակներ, դատարկ թղթապանակներ, նմանատիպ պատկերներ և շատ ավելին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/qarmin/czkawka/blob/master/czkawka_cli/README.md>:.

- Ցուցակեք կրկնօրինակները հատուկ գրացուցակներում և արդյունքները գրեք ֆայլում.:

`czkawka_cli dup {{[-d|--directories]}} {{path/to/directory1}} {{[-d|--directories]}} {{path/to/directory2}} {{[-f|--file-to-save]}} {{path/to/results.txt}}`

- Գտեք կրկնօրինակ ֆայլեր հատուկ գրացուցակներում և ջնջեք դրանք (կանխադրված՝ `NONE`):

`czkawka_cli dup {{[-d|--directories]}} {{path/to/directory}} {{[-D|--delete-method]}} {{AEN|AEO|ON|OO|HARD|NONE}}`

- Գտեք նմանատիպ տեսք ունեցող պատկեր հատուկ նմանության մակարդակով (կանխադրված՝ `High`):

`czkawka_cli image {{[-d|--directories]}} {{path/to/directory}} {{[-s|--similarity-preset]}} {{Minimal|VerySmall|Small|Medium|High|VeryHigh|Original}} {{[-f|--file-to-save]}} {{path/to/results.txt}}`

- Ցուցադրել օգնությունը.:

`czkawka_cli {{[-h|--help]}}`
