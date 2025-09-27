# chainctl

> The official CLI for Chainguard.
> More information: <https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/>.

- Authenticate to the Chainguard Platform:

`chainctl auth login`

- Logout from the Chainguard Platform:

`chainctl auth logout`

- Update to the latest version:

`chainctl update`

- List images available to your account:

`chainctl images list`

- List image repositories available to your account:

`chainctl images repos list`

- Examine the history of an image tag in chainctl (e.g., image=python tag=3):

`chainctl images history {{image}}:{{tag}}`

- List package version data from repositories available to your account (e.g., package_name=go):

`chainctl packages versions list {{package_name}}`

- Display version:

`chainctl version`
