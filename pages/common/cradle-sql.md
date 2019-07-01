# cradle sql

> Manage Cradle SQL databases.
> More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Rebuild the database schema:

`cradle sql build`

- Rebuild the database schema for a specific package:

`cradle sql build {{package_name}}`

- Empty the entire database:

`cradle sql flush`

- Empty the database tables for a specific package:

`cradle sql flush {{package_name}}`

- Populate the tables for all packages:

`cradle sql populate`

- Populate the tables for a specific package:

`cradle sql populate {{package_name}}`
