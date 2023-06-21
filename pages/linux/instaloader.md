# instaloader

> Download pictures, videos, captions, and other metadata from Instagram.
> Note: You will need to provide Instagram login information if you want high-quality media downloads.
> More information: <https://instaloader.github.io>.

- Download a profile:

`instaloader {{profile_name}}`

- Download highlights:

`instaloader --highlights {{profile_name}}`

- Download posts with geotags (if available), suppressing any user interaction:

`instaloader --quiet --geotags {{profile_name}}`

- Specify a user agent for HTTP requests:

`instaloader --user-agent {{user_agent}} {{profile_name}}`

- Specify login info and download posts (useful for private profiles):

`instaloader --login {{username}} --password {{password}} {{profile_name}}`

- Skip a target if the first downloaded file has been found (useful for updating Instagram archives):

`instaloader --fast-update {{profile_name}}`

- Download stories and IGTV videos (login required):

`instaloader --login {{username}} --password {{password}} --stories --igtv {{profile_name}}`

- Download all types of posts (login required):

`instaloader --login {{username}} --password {{password}} --stories --igtv --highlights {{profile_name}}`
