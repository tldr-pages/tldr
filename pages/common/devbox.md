# devbox

> Easily create isolated shells for development.<br>
> Full docs: https://www.jetpack.io/devbox/docs/devbox_global/.

- Quickly Find packages:

`devbox search {{package_name}}`

- Exhaustively find package versions:

`devbox search {{package_name}} --show-all`

- Install a package system wide:

```
devbox global add {{package_name}}@{{version_number}}
devbox global install
```

- Install package for just this project:

```
devbox init
devbox add {{package_name}}@{{version_number}}
devbox shell
```