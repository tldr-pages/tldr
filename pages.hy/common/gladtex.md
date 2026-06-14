#գլադտեքս

> HTML ֆայլերի LaTeX բանաձևի նախապրոցեսոր:.
> Այն փոխակերպում է LaTeX բանաձևերը պատկերների:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/gladtex>:.

- Փոխարկել HTML:

`gladtex {{path/to/input.htex}}`

- Փոխարկված ֆայլը պահեք որոշակի [o] ելքային ֆայլում՝:

`gladtex {{path/to/input.htex}} -o {{path/to/output.html}}`

- Պահպանեք ստեղծված պատկերները որոշակի [d] գրացուցակում.:

`gladtex {{path/to/input.htex}} -d {{path/to/image_output_directory}}`

- Սահմանեք պատկերի [r] լուծումը (dpi-ով, լռելյայն 100 է):

`gladtex {{path/to/input.htex}} -r {{resolution}}`

- [k]պահեք LaTeX ֆայլերը փոխարկումից հետո.:

`gladtex {{path/to/input.htex}} -k`

- Սահմանեք պատկերների [b] ֆոն և [f] նախապատկերի գույնը.:

`gladtex {{path/to/input.htex}} -b {{background_color}} -f {{foreground_color}}`

- Փոխակերպեք Markdown-ը HTML-ի՝ օգտագործելով `pandoc` և `gladtex`:

`pandoc {{[-s|--standalone]}} {{[-t|--to]}} html --gladtex {{path/to/input.md}} | gladtex -o {{path/to/output.html}}`
