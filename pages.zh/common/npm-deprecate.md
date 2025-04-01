# npm deprecate

> 标记某个 `npm` 包的某个版本或版本范围为已弃用。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-deprecate/>.

- 标记包的特定版本为已弃用：

`npm deprecate {{package_name}}@{{version}} "{{deprecation_message}}"`

- 标记包的版本范围为已弃用：

`npm deprecate {{package_name}}@"<{{version_range}}" "{{deprecation_message}}"`

- 取消标记包的特定版本为已弃用：

`npm deprecate {{package_name}}@{{version}} ""`