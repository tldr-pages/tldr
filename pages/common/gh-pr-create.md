# gh pr create

> Manage GitHub pull requests.
> More information: <https://cli.github.com/manual/gh_pr_create>.

- Interactively create a pull request:

`gh pr create`

- Create a pull request, determining the title and description from the commit messages of the current branch:

`gh pr create {{[-f|--fill]}}`


- Create a draft pull request:

`gh pr create {{[-d|--draft]}}`

- Create a pull request specifying the base branch, title, and description:

`gh pr create {{[-B|--base]}} {{base_branch}} {{[-t|--title]}} "{{title}}" {{[-b|--body]}} "{{body}}"`

- Start opening a pull request in the default web browser:

`gh pr create {{[-w|--web]}}`

- 基于当前分支创建PR，与基础分支比较，并在编辑器中填写PR信息：
  gh pr create

- 创建PR并指定标题和描述：
  gh pr create --title "标题" --body "描述"

- 创建PR并指定目标分支：
  gh pr create --base 目标分支 --head 源分支

- 创建PR并指定审核者：
  gh pr create --reviewer username1,username2

- 创建PR并指定负责人：
  gh pr create --assignee username1,username2

- 创建PR并添加标签：
  gh pr create --label bug,enhancement

- 创建PR并同时指定审核者、负责人和标签：
  gh pr create --reviewer team-name,username --assignee username --label "priority: high"

- 在浏览器中创建PR：
  gh pr create --web