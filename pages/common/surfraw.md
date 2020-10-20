# surfraw

> Surfraw is a CLI to query a variety of web search engines.
> It consists of a collection of elvi, each of which knows how to search a specific website.
> More information: <http://surfraw.org>.

- Display the list of supported website search scripts (elvi):

`surfraw -elvi`

- Search using an elvi and open the results page in the browser:

`surfraw {{elvi_name}} {{search_terms}}`

- Show the elvi description and specific options using the alias:

`sr {{elvi_name}} -local-help`

- Search using an elvi with specific options and open the results page in the browser:

`sr {{elvi_name}} {{elvi_options}} {{search_terms}}`

- Print the search URL instead of passing it to the browser:

`surfraw -print {{elvi}} "{{search_terms}}"`
