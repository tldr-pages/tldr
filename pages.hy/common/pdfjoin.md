# pdf միանալ

> PDF-ի միաձուլման ծրագիր, որը հիմնված է pdfjam-ի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/pdfjam/pdfjam-extras>:.

- Միավորել երկու PDF ֆայլ մեկի մեջ լռելյայն «միացել» վերջածանցով.:

`pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}`

- Միավորել յուրաքանչյուր տվյալ ֆայլի առաջին էջը միասին.:

`pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}`

- Պահպանեք 3-ից 5-րդ էջերը, որին հաջորդում է 1-ին էջը նոր PDF-ում՝ հատուկ վերջածանցով.:

`pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}`

- Միավորել էջի ենթատիրույթները երկու PDF-ից.:

`pdfjoin /{{path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}`
