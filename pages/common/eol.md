# eol

> CLI to show end-of-life dates (EoLs) for an (ever increasing) number of products (e.g. Programming Languages, Frameworks, Devices, Operating Systems, Desktop Applications, ...).
> More information: <https://github.com/hugovk/norwegianblue>.

- Get help:

`eol -h`

- List all available products:

`eol`

- Get eols of a given product:

`eol {{product}}`

- Open product webpage on endoflie.date:

`eol {{product}} -w`

- Get eols of multiple products all at once:

`eol {{product1}} {{product2}} {{product3}}`

- Get eols of a product as markdown:

`eol {{product}} -f markdown`

- Get eols of a product as csv:

`eol {{product}} -f csv`

- Get eols of a multiple products as a single markdown file:

`eol {{product1}} {{product2}} {{product3}} -f markdown > eol_report.md`
