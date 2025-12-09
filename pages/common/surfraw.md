# surfraw

> Query a variety of web search engines.
> Consists of a collection of elvi, each of which knows how to search a website.
> More information: <https://manned.org/surfraw>.

- Display the list of supported website search scripts (elvi):

`surfraw -elvi`

- Open the elvi's results page for a specific search in the browser:

`surfraw {{elvi_name}} "{{search_terms}}"`

- Display an elvi description and its specific options:

`surfraw {{elvi_name}} {{[-lh|-local-help]}}`

- Search using an elvi with specific options and open the results page in the browser:

`surfraw {{elvi_name}} {{elvi_options}} "{{search_terms}}"`

- Display the URL to the elvi's results page for a specific search:

`surfraw -print {{elvi_name}} "{{search_terms}}"`

- Search using the alias:

`sr {{elvi_name}} "{{search_terms}}"`
