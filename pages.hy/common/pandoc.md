#պանդոկ

> Փոխարկել փաստաթղթերը տարբեր ձևաչափերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://pandoc.org/MANUAL.html>:.

- Փոխակերպեք Markdown ֆայլը PDF-ի՝ օգտագործելով `pdflatex` (ձևաչափերը որոշվում են ֆայլի ընդլայնումներով).:

`pandoc {{path/to/input.md}} {{[-o|--output]}} {{path/to/output.pdf}}`

- Փոխարկեք արդյունքը մեկ այլ հրամանից PDF-ի, օգտագործելով հատուկ PDF շարժիչ.:

`{{command}} | pandoc {{[-f|--from]}} {{input_format}} --pdf-engine {{tectonic|weasyprint|typst|...}} {{[-o|--output]}} {{path/to/output.pdf}}`

- Փոխակերպեք առանձին ֆայլի համապատասխան վերնագրերով/ստորատակներով (LaTeX, HTML և այլն):

`pandoc {{path/to/input.md}} {{[-s|--standalone]}} {{[-o|--output]}} {{path/to/output.html}}`

- Ձեռքով նշեք ձևաչափերը (գերակայող ավտոմատ ձևաչափի հայտնաբերումը, օգտագործելով ֆայլի անվան ընդլայնումը, կամ երբ ընդլայնում չկա).:

`pandoc {{[-f|--from]}} {{docx|...}} {{path/to/input}} {{[-t|--to]}} {{pdf|...}} {{[-o|--output]}} {{path/to/output}}`

- Փոխակերպեք փաստաթուղթը՝ օգտագործելով Lua script (տե՛ս <https://pandoc.org/lua-filters.html> լրացուցիչ տեղեկությունների համար).:

`pandoc {{path/to/input}} {{[-L|--lua-filter]}} {{path/to/filter.lua}} {{[-o|--output]}} {{path/to/output}}`

- Փոխակերպեք հեռավոր HTML ֆայլը նշագրման և արդյունքը տպեք `stdout`:

`pandoc {{[-f|--from]}} html {{[-t|--to]}} markdown {{https://example.com}}`

- Թվարկեք բոլոր աջակցվող մուտքային ձևաչափերը.:

`pandoc --list-input-formats`

- Թվարկեք բոլոր աջակցվող ելքային ձևաչափերը.:

`pandoc --list-output-formats`
