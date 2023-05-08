# gallery-dl

> Download image galleries and collections from several image hosting sites.
> More information: <https://github.com/mikf/gallery-dl>.

- Download images from the specified URL:

`gallery-dl "{{url}}"`

- Get the direct URL of an image from a site supporting authentication with username and password:

`gallery-dl --get-urls --username {{username}} --password {{password}} "{{url}}"`

- Filter manga chapters by chapter number and language:

`gallery-dl --chapter-filter "10 <= chapter < 20" -o "lang=fr" "https://mangadex.org/title/59793dd0-a2d8-41a2-9758-8197287a8539"`
