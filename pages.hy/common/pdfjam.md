# pdfjam

> Shell frontend-ը LaTeX pdfpages փաթեթի համար՝ PDF-ների միախառնման համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/pdfjam/pdfjam/blob/master/doc/pdfjam-help.txt>:.

- Միավորել երկու (կամ ավելի) PDF ֆայլեր.:

`pdfjam {{path/to/file1.pdf path/to/file2.pdf ...}} {{[-o|--outfile]}} {{path/to/output_file.pdf}}`

- Միավորել յուրաքանչյուր ֆայլի առաջին էջը միասին.:

`pdfjam {{path/to/file1.pdf 1 path/to/file2.pdf 1 ...}} {{[-o|--outfile]}} {{path/to/output_file.pdf}}`

- Միավորել ենթատիրույթները երկու PDF-ից.:

`pdfjam {{path/to/file1.pdf 3-5,1}} {{path/to/file2.pdf 4-6}} {{[-o|--outfile]}} {{path/to/output_file.pdf}}`

- Ստորագրեք A4 էջը (դելտան կարգավորեք բարձրության վրա այլ ձևաչափերի համար) սկանավորված ստորագրությամբ՝ դրանք ծածկելով.:

`pdfjam {{path/to/file.pdf}} {{path/to/signature}} --fitpaper true {{[-o|--outfile]}} {{path/to/signed.pdf}} --nup "{{1x2}}" --delta "{{0 -842pt}}"`

- Մուտքային ֆայլից էջերը դասավորեք շքեղ 2x2 ցանցի մեջ.:

`pdfjam {{path/to/file.pdf}} --nup {{2x2}} --suffix {{4up}} --preamble '{{\usepackage{fancyhdr} \pagestyle{fancy}}}'`

- Փոխեք էջերի հերթականությունը յուրաքանչյուր տվյալ ֆայլում և միացրեք դրանք.:

`pdfjam {{path/to/file1.pdf last-1 path/to/file2.pdf last-1 ...}} --suffix {{reversed}}`
