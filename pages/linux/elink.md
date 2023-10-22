# elink

> Look up precomputed neighbors within a database, or find associated records in other databases.
> It is part of the `edirect` package.
> More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search pubmed then find related sequences:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}" | elink -target nuccore`

- Search nucleotide then find related biosamples:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}" | elink -target biosample`
