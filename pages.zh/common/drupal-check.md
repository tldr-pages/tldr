# drupal-check

> 检查 Drupal PHP 代码中的弃用项。
> 更多信息：<https://github.com/mglaman/drupal-check>.

- 检查特定目录中的代码弃用项：

`drupal-check {{path/to/directory}}`

- 检查代码时排除逗号分隔的目录列表：

`drupal-check --exclude-dir {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}`

- 不显示进度条：

`drupal-check --no-progress {{path/to/directory}}`

- 执行静态分析以检测不良编码实践：

`drupal-check --analysis {{path/to/directory}}`
