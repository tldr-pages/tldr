# elink

> Elink looks up precomputed neighbors within a database, or finds associated records in other databases.
> It is part of the edirect package: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search pubmed and then find related sequences:

`esearch -db pubmed -query "selective serotonin reuptake inhibitor" | elink -target nuccore`

- Search nucleotide and then find related biosamples:

`esearch -db nuccore -query "insulin [PROT] AND rodents [ORGN]" | elink -target biosample`

