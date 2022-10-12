# esearch

> Perform a new Entrez search using terms in indexed fields.
> It is part of the `edirect` package.
> More information: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search the pubmed database for selective serotonin reuptake inhibitor:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}"`

- Search the nucleotide database for sequences whose metadata contain insulin and rodents:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`
