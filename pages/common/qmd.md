# qmd

> Search local Markdown documents using keywords or semantic similarity.
> More information: <https://github.com/tobi/qmd>.

- Add a directory of Markdown documents as a named collection:

`qmd collection add {{path/to/directory}} --name {{collection_name}}`

- Search indexed documents using keywords:

`qmd search "{{search_terms}}"`

- Search for keywords within a specific collection:

`qmd search "{{search_terms}}" {{[-c|--collection]}} {{collection_name}}`

- Generate embeddings for semantic search:

`qmd embed`

- Search with query expansion, keyword and vector matching, and reranking:

`qmd query "{{query}}"`

- Retrieve an indexed document by its collection and path:

`qmd get "{{collection_name}}/{{path/to/file.md}}"`

- Re-index all collections after documents change:

`qmd update`

- Show index and collection status:

`qmd status`
