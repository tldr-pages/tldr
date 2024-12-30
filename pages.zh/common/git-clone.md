# git clone

> 克隆一个现有的代码库。
> 更多信息：<https://git-scm.com/docs/git-clone>。

- 将现有的代码库克隆到一个新目录中（默认目录为代码库名称）：

`git clone {{remote_repository_location}} {{path/to/directory}}`

- 克隆一个现有的代码库及其子模块：

`git clone --recursive {{remote_repository_location}}`

- 仅克隆现有代码库的 `.git` 目录：

`git clone --no-checkout {{remote_repository_location}}`

- 克隆一个本地代码库：

`git clone --local {{path/to/local/repository}}`

- 安静地克隆：

`git clone --quiet {{remote_repository_location}}`

- 仅克隆现有代码库，获取默认分支上最近的 10 次提交（有助于节省时间）：

`git clone --depth {{10}} {{remote_repository_location}}`

- 仅克隆现有代码库，获取特定分支：

`git clone --branch {{name}} --single-branch {{remote_repository_location}}`

- 使用特定的 SSH 命令克隆现有代码库：

`git clone --config core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{remote_repository_location}}`