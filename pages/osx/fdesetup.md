# fdesetup

> Set and retrieve FileVault related information.
> More information: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

- List current FileVault enabled users:

`sudo fdesetup list`

- Get current FileVault status:

`fdesetup status`

- Add FileVault enabled user:

`sudo fdesetup add -usertoadd {{user1}}`

- Enable FileVault:

`sudo fdesetup enable`

- Disable FileVault:

`sudo fdesetup disable`
