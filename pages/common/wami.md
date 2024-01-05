# wami

> A tool that recommends suitable programs for specific tasks. Open-source, easy to use.
> More information: <https://github.com/evait-security/wami>.

- Search the lake and find expanded results in all categories in descending order:

`wami --show-[a]ll --[S]ort desc --[s]earch-all {{search_string}}`

- Search GitHub to find expanded results, displayed in descending order:

`wami --show-[a]ll --[S]ort desc --github {{search_string}}`

- Search GitHub for topics that match the search string:

`wami --list-topics {{search_string}}`

- Search the lake for a tool used in pentests to query for default credentials and order desc to get the first match at the bottom:

`wami --[S]ort desc --[s]earch-all pentest credential default`
