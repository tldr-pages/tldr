# instaloader

> Download pictures, videos, captions, and other metadata from Instagram.
> Note: You will need to provide instagram login information if you want high quality media downloads.
> More information: <https://instaloader.github.io>.

- Download a profile (defaults to regular posts):

`instaloader {{profile_name}}`

- Download posts with geotags (if available) while suppressing any user interaction:

`instaloader --quiet --geotags {{profile_name}}`

- Specify login info and download posts (useful for private profiles):

`instaloader --login {{username}} --password {{password}} {{profile_name}}`

- Skip a target if the first downloaded file has been found (useful for Instagram archives):

`instaloader --fast-update {{profile_name}}`

- Also Download stories and IGTV videos (login required):

`instaloader --login {{username}} --password {{password}} --stories --igtv {{profile_name}}`

- Also Download highlights:

`instaloader --highlights {{profile_name}}`

- Download all types of posts (login required):

`instaloader --login {{username}} --password {{password}} --stories --igtv --highlights {{profile_name}}`
