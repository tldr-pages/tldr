# conan list

> List recipes, revisions, or packages in the local cache or on remotes.
> More information: <https://docs.conan.io/2/reference/commands/list.html>.

- List all recipes in the local cache:

`conan list "*"`

- List all binary packages of a specific recipe:

`conan list {{package_name}}/{{version}}:*`

- List a recipe as it exists on a remote:

`conan list {{package_name}}/{{version}} --remote={{remote_name}}`

- Print the result in JSON format:

`conan list {{package_name}}/{{version}} --format=json`
