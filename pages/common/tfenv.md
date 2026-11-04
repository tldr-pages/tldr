# tfenv

> Install, uninstall, or switch between Terraform versions.
> Note: Automatically uses the version from `.terraform-version`, if present.
> See also: `terraform`, `asdf`.
> More information: <https://github.com/tfutils/tfenv#usage>.

- Install/uninstall a specific version:

`tfenv {{install|uninstall}} {{terraform_version}}`

- Install the latest version matching a `regex`:

`tfenv install latest:{{regex}}`

- Install the minimum version required by the current workspace:

`tfenv install min-required`

- Switch to a version and set it as default:

`tfenv use {{terraform_version}}`

- List available remote versions:

`tfenv list-remote`

- List installed versions:

`tfenv list`

- Pin the currently used version in `.terraform-version`:

`tfenv pin`
