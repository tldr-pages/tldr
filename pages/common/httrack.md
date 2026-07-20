# httrack

> Download websites for offline browsing.
> More information: <https://www.httrack.com/html/fcguide.html>.

- Mirror a website:

`httrack {{https://example.com}}`

- Mirror a website to a specific directory:

`httrack {{https://example.com}} -O {{path/to/output_directory}}`

- Continue an interrupted mirror using the cache:

`httrack {{https://example.com}} -O {{path/to/output_directory}} -i`

- Limit the recursion depth:

`httrack {{https://example.com}} -r{{5}}`

- Mirror all links from the first-level pages:

`httrack {{https://example.com}} -Y`

- Exclude ZIP files while mirroring:

`httrack {{https://example.com}} "-*.zip"`
