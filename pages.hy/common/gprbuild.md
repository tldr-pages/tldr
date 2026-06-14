# gprbuild

> Բարձր մակարդակի կառուցման գործիք Ada-ով և այլ լեզուներով գրված նախագծերի համար (C/C++/Fortran):.
> Լրացուցիչ տեղեկություններ. <https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>:.

- Կառուցեք նախագիծ (ենթադրելով, որ ընթացիկ գրացուցակում գոյություն ունի միայն մեկ `*.gpr` ֆայլ).:

`gprbuild`

- Կառուցեք կոնկրետ [P]նախագծային ֆայլ.:

`gprbuild -P {{project_name}}`

- Մաքրել շինարարական աշխատանքային տարածքը.:

`gprclean`

- Տեղադրեք կազմված երկուականներ.:

`gprinstall --prefix {{path/to/installation_directory}}`
