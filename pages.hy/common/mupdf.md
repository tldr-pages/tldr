# mupdf

> Թեթև PDF, XPS և էլեկտրոնային գրքերի դիտիչ:.
> Լրացուցիչ տեղեկություններ. <https://mupdf.readthedocs.io/en/latest/tools/mupdf-gl.html>:.

- Բացեք PDF-ը առաջին էջում.:

`mupdf {{path/to/file}}`

- Բացեք PDF էջ 3:

`mupdf {{path/to/file}} {{3}}`

- Բացեք գաղտնաբառով ապահովված PDF.:

`mupdf -p {{password}} {{path/to/file}}`

- Բացեք PDF նախնական խոշորացման մակարդակով, որը նշված է որպես DPI, 72:

`mupdf -r {{72}} {{path/to/file}}`

- Բացեք PDF շրջված գույնով.:

`mupdf -I {{path/to/file}}`

- Բացեք PDF մգեցված կարմիր #FF0000 (վեցանկյուն գույնի շարահյուսություն RRGGBB):

`mupdf -C {{FF0000}}`

- Բացեք PDF առանց հակաալիզացման (0 = անջատված, 8 = լավագույնը):

`mupdf -A {{0}}`
