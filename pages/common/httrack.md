# httrack

> Download full websites to your computer.
> More information: <https://www.httrack.com/html/fcguide.html>.

- Download a website:

`httrack {{https://example.com}}`

- Download a website and save it to a specific folder:

`httrack {{https://example.com}} -O {{path/to/folder}}`

- Resume a download that stopped:

`httrack --continue -O {{path/to/folder}}`

- Download a website, but skip downloading certain files (like videos):

`httrack {{https://example.com}} "-*.mp4"`

- Download a website but only follow links a certain number of pages deep:

`httrack {{https://example.com}} -r{{depth}}`
