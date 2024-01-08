# wami

> An open-source and easy-to-use tool that recommends suitable programs for specific tasks.
> More information: <https://github.com/evait-security/wami>.

- Find expanded results in all categories from the lake and [S]ort them in the specified order:

`wami --show-all -S {{asc|desc}} --search-all {{search_string}}`

- Search GitHub to find expanded results, [S]orted in descending order:

`wami --show-all -S desc --github {{search_string}}`

- Search GitHub for topics that match the search string:

`wami --list-topics {{search_string}}`

- Search the lake for a tool used in pentests to query for default credentials and [S]ort the results in descending order:

`wami -S desc --search-all pentest credential default`
