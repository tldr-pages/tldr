# conan profile

> Manage Conan profiles, which define settings and options for building packages.
> More information: <https://docs.conan.io/2/reference/commands/profile.html>.

- Auto-detect the host environment and create a `default` profile:

`conan profile detect`

- List the profiles in the cache:

`conan profile list`

- Show the aggregated configuration of the current profiles:

`conan profile show`

- Show the path of a specific profile:

`conan profile path {{profile_name}}`
