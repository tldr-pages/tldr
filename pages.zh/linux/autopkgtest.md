# autopkgtest

> 在 Debian 包上运行测试。
> 更多信息：<https://wiki.debian.org/ContinuousIntegration/autopkgtest>。

- 在当前目录中构建包并直接在系统上运行所有测试：

`autopkgtest -- {{null}}`

- 为当前目录中的包运行特定测试：

`autopkgtest --test-name={{test_name}} -- {{null}}`

- 使用 `apt-get` 下载并构建特定包，然后运行所有测试：

`autopkgtest {{package}} -- {{null}}`

- 使用新的根目录测试当前目录中的包：

`autopkgtest -- {{chroot}} {{path/to/new/root}}`

- 在不重新构建的情况下测试当前目录中的包：

`autopkgtest --no-built-binaries -- {{null}}`