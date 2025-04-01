# pio package

> 管理注册表中的包。
> 包只能在发布后的 72 小时（3 天）内删除。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/package/>.

- 从当前目录创建包 tarball：

`pio package pack --output {{path/to/package.tar.gz}}`

- 从当前目录创建并发布包 tarball：

`pio package publish`

- 发布当前目录并限制公共访问：

`pio package publish --private`

- 发布一个包：

`pio package publish {{path/to/package.tar.gz}}`

- 发布一个带有自定义发布日期（UTC）的包：

`pio package publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- 从注册表中删除所有版本的已发布包：

`pio package unpublish {{package}}`

- 从注册表中删除已发布包的特定版本：

`pio package unpublish {{package}}@{{version}}`

- 撤销删除，将包的所有版本或特定版本重新放回注册表中：

`pio package unpublish --undo {{package}}@{{version}}`
