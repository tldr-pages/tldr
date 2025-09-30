# wami

> An open-source and easy-to-use tool that recommends suitable programs for tasks.
> More information: <https://github.com/evait-security/wami>.

- Find expanded results in all categories from the lake and sort them in the specified order:

`wami {{[-a|--show-all]}} {{[-S|--sort]}} {{asc|desc}} {{[-s|--search-all]}} {{search_string}}`

- Search GitHub to find expanded results, sorted in descending order:

`wami {{[-a|--show-all]}} {{[-S|--sort]}} desc --github {{search_string}}`

- Search GitHub for topics that match the search string:

`wami --list-topics {{search_string}}`

- Search the lake for a tool used in pentests to query for default credentials and sort the results in descending order:

`wami {{[-S|--sort]}} desc {{[-s|--search-all]}} pentest credential default`
