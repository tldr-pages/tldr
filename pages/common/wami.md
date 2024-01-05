# wami - What am I

> A tool that recommends suitable programs for specific tasks. Open-source, easy to use.
> More information: <https://github.com/evait-security/wami>.

- Search the lake and find expanded results in all categories in descending order:

`wami -a -S desc -s <search-string>`

- Search GitHub to find expanded results, displayed in descending order:

`wami -a -S desc --github <search-string>`

- Search GitHub for topics that match the search string:

`wami --list-topics <search-string>`

- Search the lake for a tool used in pentests to query for default credentials and order desc to get the first match at the bottom:

`wami -S desc -s pentest credential default`
