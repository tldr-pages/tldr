# pio 包

> 管理注册表中的包。
> 包只能在发布日期后的72小时（3天）内删除。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/package/>.

- 从当前目录创建一个包的 tarball：

`pio package pack --output {{path/to/package.tar.gz}}`

- 从当前目录创建并发布一个包的 tarball：

`pio package publish`

- 发布当前目录并限制对其的公开访问：

`pio package publish --private`

- 发布一个包：

`pio package publish {{path/to/package.tar.gz}}`

- 发布一个具有自定义发布日期（UTC）的包：

`pio package publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- 从注册表中删除已发布包的所有版本：

`pio package unpublish {{package}}`

- 从注册表中删除已发布包的特定版本：

`pio package unpublish {{package}}@{{version}}`

- 撤销删除，将所有版本或特定版本的包放回注册表：

`pio package unpublish --undo {{package}}@{{version}}`