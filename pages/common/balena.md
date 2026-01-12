# balena

> Interact with the balenaCloud, openBalena, and the balena API.
> More information: <https://docs.balena.io/reference/balena-cli/latest/>.

- Log in to the balenaCloud account:

`balena login`

- Create a balenaCloud or openBalena application:

`balena app create {{app_name}}`

- List all balenaCloud or openBalena applications within the account:

`balena apps`

- List all devices associated with the balenaCloud or openBalena account:

`balena devices`

- Flash a balenaOS image to a local drive:

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
