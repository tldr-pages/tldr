# feroxbuster

> Brute-forces hidden paths on web servers and more.
> More information: <https://github.com/epi052/feroxbuster>.

- Discover specific directories and files that match in the wordlist with extensions and 100 threads and a random user agent:

`feroxbuster --url "{{https://example.com/}}" --wordlist {{path/to/file}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- Enumerate directories without recursion through a specific proxy:

`feroxbuster --url "{{https://example.com/}}" --wordlist {{path/to/file}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- Find links in webpages:

`feroxbuster --url "{{https://example.com/}}" --extract-links`

- Filter by status code and number of chars:

`feroxbuster -u {{https://example.com/}} --filter-status 301 -S 4092`
