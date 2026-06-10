#գրագիր

> Փոխարկեք տեքստային ֆայլերը PostScript, HTML, RTF, ANSI և overstrikes:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/enscript>:.

- Ստեղծեք PostScript ֆայլ տեքստային ֆայլից.:

`enscript {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- Ստեղծեք ֆայլ այլ լեզվով, քան PostScript-ը.:

`enscript {{path/to/input_file}} {{[-w|--language]}} {{html|rtf|...}} {{[-o|--output]}} {{path/to/output_file}}`

- Ստեղծեք PostScript ֆայլ լանդշաֆտային դասավորությամբ՝ էջը բաժանելով սյունակների (առավելագույնը 9):

`enscript {{path/to/input_file}} --columns {{num}} {{[-r|--landscape]}} {{[-o|--output]}} {{path/to/output_file}}`

- Ցուցադրել հասանելի շարահյուսական ընդգծող լեզուները և ֆայլի ձևաչափերը.:

`enscript --help-highlight`

- Ստեղծեք PostScript ֆայլ՝ շարահյուսական ընդգծմամբ և գույնով նշված լեզվի համար.:

`enscript {{path/to/input_file}} --color 1 {{[-E|--highlight]}} {{language}} {{[-o|--output]}} {{path/to/output_file}}`
