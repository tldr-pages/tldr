# instaloader

> Download pictures, videos, captions, and other metadata from Instagram.
> Note: You will need to provide instagram login information if you want high quality media downloads.
> More information: <https://instaloader.github.io>.

- Download a profile (defaults to regular posts):

`instaloader {{profilename}}`

- Specify login info and download posts:

`instaloader --login {{username}} --password {{password}} {{profilename}}`

- Skip a target if a downloaded file has been found (useful for Instagram archives):

`instaloader --fast-update {{profilename}}`

- Download stories only:

`instaloader --stories {{profilename}}`

- Download IGTV videos:

`instaloader --igtv {{profilename}}`

- Download highlights:

`instaloader --highlights {{profilename}}`

- Download all types of posts:

`instaloader --stories --igtv --highlights {{profilename}}`
