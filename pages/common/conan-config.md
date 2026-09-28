# conan-config

> Manage the Conan configuration (remotes, profiles, core conf) stored in the Conan home folder.
> More information: <https://docs.conan.io/2/reference/commands/config.html>.

- Show the path of the Conan home folder:

`conan config home`

- Show all available configurations, both core and tools:

`conan config list`

- Show the value of configuration items matching a pattern:

`conan config show {{pattern}}`

- Install a configuration from a Git repository URL, a local folder or a (local or remote) zip file:

`conan config install {{git_url|folder|zip_file}}`

- Install a configuration from a specific type of source, e.g. only if it is a Git repository:

`conan config install --type git {{git_url}}`

- Install only part of a configuration repository into a sub-folder of the Conan home:

`conan config install --source-folder {{subfolder}} --target-folder {{target_folder}} {{git_url}}`
