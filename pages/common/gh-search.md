# gh search

> Search across all of GitHub.
> More information: <https://cli.github.com/manual/gh_search>.

- Search for code containing specific keywords:

`gh search code {{keyword1 keyword2 ...}}`

- Search for issues with a specific phrase:

`gh search issues "{{search_phrase}}"`

- Search commits by a specific author:

`gh search commits --author {{username}}`

- Search pull requests assigned to yourself that are still open:

`gh search prs --assignee @me --state open`

- Search repositories in an organization by topic:

`gh search repos --owner {{org_name}} --topic {{topic_name}}`

- Search issues without a certain label (Unix-like systems):

`gh search issues -- "{{search_query}} -label:{{label_name}}"`

- Search issues without a certain label (PowerShell):

`gh --% search issues -- "{{search_query}} -label:{{label_name}}"`

- Open the search query in the web browser:

`gh search {{subcommand}} {{[-w|--web]}} {{query}}`
