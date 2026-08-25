# powerpnt

> Microsoft Office's presentation application.
> More information: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=powerpoint%2C_powerpoint_viewer>.

- Launch the presentation application:

`powerpnt`

- Create a new [b]lank presentation:

`powerpnt /b`

- Create a [n]ew presentation from a template:

`powerpnt /n {{path\to\file.potm}}`

- [o]pen one or more files:

`powerpnt /o {{path\to\file1.pptx path\to\file2.pptx ...}}`

- Open a file in [s]lideshow mode:

`powerpnt /s {{path\to\file.pptx}}`

- Open a presentation, then execute a specific [m]acro:

`powerpnt /m {{path\to\file.pptm}} "{{MacroName}}"`

- Print a presentation via the Print dialog:

`powerpnt /pwo {{path\to\file.pptx}}`

- Directly [p]rint a presentation [t]o a specific printer:

`powerpnt /pt {{printer_name}} {{path\to\file.pptx}}`
