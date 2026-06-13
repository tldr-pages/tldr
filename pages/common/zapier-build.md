# zapier build

> Build a pushable `zip` of a Zapier integration.
> More information: <https://platform.zapier.com/reference/cli#build>.

- Create a build:

`zapier build`

- Disable smart file inclusion (will only include files required by `index.js`):

`zapier build --disable-dependency-detection`

- Show extra debugging output:

`zapier build {{[-d|--debug]}}`
