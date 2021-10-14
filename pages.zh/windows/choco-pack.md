# choco pack

> 将 nuspec 打包到已编译的 nupkg.
> 更多信息：<https://chocolatey.org/docs/commands-pack>.

- 将 nuspec 打包到已编译的 nupkg:

`choco pack {{nuspec 的路径}}`

- 将 nuspec 打包到已编译的 nupkg, 并指定生成的版本：

`choco pack {{nuspec 的路径}} --version {{版本号}}`

- 将 nuspec 打包到已编译的 nupkg, 并输出到指定的目录：

`choco pack {{nuspec 的路径}} --output-directory {{输出目录的路径}}`
