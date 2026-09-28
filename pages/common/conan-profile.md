# conan profile

> Create, list and inspect configuration profiles that define settings and options for packages.
> More information: <https://docs.conan.io/2/reference/commands/profile.html>.

- Auto-detect the current machine settings and create a default profile:

`conan profile detect`

- List all profiles available in the cache:

`conan profile list`

- Show the contents of a specific profile:

`conan profile show -pr={{profile_name}}`

- Show the path of a profile folder or file:

`conan profile path {{profile_name}}`
