# act

> 使用Docker本地运行GitHub Actions
> 更多信息: <https://github.com/nektos/act>.

- 列出可用的actions清单:

`act -l`

- 运行默认event:

`act`

- 运行指定event:

`act {{event_type}}`

- 运行指定action:

`act -a {{action_id}}`

- 非实际运行actions (i.e. dry-run模式):

`act -n`

- 展示详细记录:

`act -v`
