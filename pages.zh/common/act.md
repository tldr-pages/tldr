# act

> 使用Docker本地运行GitHub Actions
> act详见: <https://github.com/nektos/act>.
> GitHub Actions详见: <https://developer.github.com/actions/>.

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
