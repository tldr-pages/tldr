# esearch

> Esearch performs a new Entrez search using terms in indexed fields.
> It requires a `-db` argument for the database name and uses `-query` for the search terms.
> It is part of the edirect package: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Search pubmed:

`esearch -db pubmed -query "selective serotonin reuptake inhibitor"`

- Search nucleotide:

`esearch -db nuccore -query "insulin [PROT] AND rodents [ORGN]"`
