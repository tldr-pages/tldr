# instaloader

> Download pictures, videos, captions, and other metadata from Instagram.
> Note: You will need to provide instagram login information if you want high quality media downloads.
> More information: <https://instaloader.github.io>.

- Download a profile (defaults to regular posts):

`instaloader {{profile_name}}`

- Specify login info and download posts:

`instaloader --login {{username}} --password {{password}} {{profile_name}}`

- Skip a target if the first downloaded file has been found (useful for Instagram archives):

`instaloader --fast-update {{profile_name}}`

- Download stories only:

`instaloader --stories {{profile_name}}`

- Download IGTV videos:

`instaloader --igtv {{profile_name}}`

- Download highlights:

`instaloader --highlights {{profile_name}}`

- Download all types of posts:

`instaloader --stories --igtv --highlights {{profile_name}}`
