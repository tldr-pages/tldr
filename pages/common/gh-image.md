# gh image

> Upload images to GitHub from the command line and print their Markdown references.
> See also: `gh extension`.
> More information: <https://github.com/drogers0/gh-image>.

- Upload one or more images, inferring the repository from the current git remote:

`gh image {{path/to/image1.png path/to/image2.png ...}}`

- Upload an image to a specific repository:

`gh image --repo {{owner/repository}} {{path/to/image.png}}`

- Upload an image using a specific session token:

`gh image --token {{session_token}} {{path/to/image.png}}`

- Extract the GitHub session token from the browser and print it:

`gh image extract-token`

- Verify that a session token is valid and print the associated username:

`gh image check-token`
