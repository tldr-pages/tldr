# waybackurls

> Fetch URLs from the Wayback Machine for a given domain.
> More information: <https://github.com/tomnomnom/waybackurls>.

- Fetch all known URLs for a domain:

`echo "{{example.com}}" | waybackurls`

- Fetch URLs for a domain, excluding [no-sub]domain results:

`echo "{{example.com}}" | waybackurls -no-subs`

- Fetch URLs with the [dates] they were crawled:

`echo "{{example.com}}" | waybackurls -dates`

- Fetch URLs for multiple domains from a file:

`cat {{path/to/domains.txt}} | waybackurls`

- Fetch archived [get-versions] of a specific URL:

`echo "{{https://example.com/page}}" | waybackurls -get-versions`

- Fetch URLs and save results to a file:

`echo "{{example.com}}" | waybackurls > {{path/to/output.txt}}`
