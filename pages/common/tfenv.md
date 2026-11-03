# tfenv

> Install, uninstall, or switch between Terraform versions.
> Supports version numbers like "1.5.7" and keywords like "latest", "min-required" or "latest-allowed".
> Automatically uses the Terraform version from a `.terraform-version` file, if present.
> See also: `terraform`, `asdf`.
> More information: <https://github.com/tfutils/tfenv#usage>.

- Install/uninstall a specific version of Terraform:

`tfenv {{install|uninstall}} {{terraform_version}}`

- Install the latest version of Terraform matching a `regex`:

`tfenv install latest:{{regex}}`

- Install the minimum version of Terraform required by the configuration files in the current directory:

`tfenv install min-required`

- Switch the Terraform version to use (also sets it as the default version):

`tfenv use {{terraform_version}}`

- List remote versions available for install:

`tfenv list-remote`

- List installed versions:

`tfenv list`

- Create a `.terraform-version` file in the current directory pinning the currently used version:

`tfenv pin`
