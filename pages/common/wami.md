# wami

> A tool that recommends suitable programs for specific tasks. Open-source, easy to use.
> More information: <https://github.com/evait-security/wami>.

- Find expanded results in all categories from the lake and [s]ort them in descending order:

`wami --show-all -S desc --search-all {{search_string}}`

- Search GitHub to find expanded results, [s]orted in descending order:

`wami --show-all -S desc --github {{search_string}}`

- Search GitHub for topics that match the search string:

`wami --list-topics {{search_string}}`

- Search the lake for a tool used in pentests to query for default credentials and [s]ort the results in descending o>

`wami -S desc --search-all pentest credential default`
