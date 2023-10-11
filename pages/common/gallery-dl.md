# gallery-dl

> Download image galleries and collections from several image hosting sites.
> More information: <https://github.com/mikf/gallery-dl>.

- Download images from the specified URL:

`gallery-dl "{{url}}"`

- Retrieve pre-existing cookies from your web browser (useful for sites that require login):

`gallery-dl --cookies-from-browser {{browser}} "{{url}}"`

- Get the direct URL of an image from a site supporting authentication with username and password:

`gallery-dl --get-urls --username {{username}} --password {{password}} "{{url}}"`

- Filter manga chapters by chapter number and language:

`gallery-dl --chapter-filter "{{10 <= chapter < 20}}" --option "lang={{language_code}}" "{{url}}"`
