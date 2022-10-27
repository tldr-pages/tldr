# einfo

> Provides the number of records indexed in each field of a given database, the date of the last update of the database, and the available links from the database to other Entrez databases.
> More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Print all database names:

`einfo -dbs`

- Print all information of the protein database in XML format:

`einfo -db {{protein}}`

- Print all fields of the nuccore database:

`einfo -db {{nuccore}} -fields`

- Print all links of the protein database:

`einfo -db {{protein}} -links`
