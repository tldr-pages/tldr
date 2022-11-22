# feroxbuster

> Brute-forces hidden paths on web servers and more.
> More information: <https://github.com/epi052/feroxbuster>.

- Discover directories and files that match in the wordlist with e[x]tensions and 100 [t]hreads and a random user [A]gent:

`feroxbuster -u {{https://example.com/}} -w {{path/to/file}} -t 100 -x php,txt -A`

- Enumerate directories without recursion through a proxy:

`feroxbuster -u {{https://example.com/}} -w {{path/to/file}} --no-recursion --proxy http://127.0.0.1:8080`

- Find links in webpages:

`feroxbuster -u {{https://example.com/}} --extract-links`

- Filter by status code and number of chars:

`feroxbuster -u {{https://example.com/}} --filter-status 301 -S 4092`
