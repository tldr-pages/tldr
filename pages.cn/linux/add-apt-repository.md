# add-apt-repository

> apt仓库管理.

- 添加一个新的apt仓库:

`add-apt-repository {{repository_spec}}`

- 移除一个apt仓库:

`add-apt-repository --remove {{repository_spec}}`

- 添加一个仓库并更新缓存:

`add-apt-repository --update {{repository_spec}}`

- 允许从指定仓库下载源码:

`add-apt-repository --enable-source {{repository_spec}}`
