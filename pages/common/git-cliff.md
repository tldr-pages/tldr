# git cliff

> A highly customizable changelog generator.
> More information: <https://git-cliff.org/docs/usage/args>.

- Generate a changelog from all commits in a Git repository and save it to `CHANGELOG.md`:

`git cliff > {{CHANGELOG.md}}`

- Generate from commits starting from the latest tag and print to `stdout`:

`git cliff {{-l|--latest}}`

- Generate from commits that belong to the current tag (use `git checkout` on a tag before this):

`git cliff --current`

- Generate from commits that do not belong to a tag:

`git cliff {{-u|--unreleased}}`

- Write the default config file to `cliff.toml` in the current directory:

`git cliff {{-i|--init}}`
