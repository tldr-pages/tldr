# drupal-check

> 检查Drupal PHP代码中的弃用情况。
> 更多信息：<https://github.com/mglaman/drupal-check>。

- 检查特定目录中的代码是否有弃用：

`drupal-check {{path/to/directory}}`

- 检查代码，排除以逗号分隔的目录列表：

`drupal-check --exclude-dir {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}`

- 不显示进度条：

`drupal-check --no-progress {{path/to/directory}}`

- 执行静态分析以检测不良编码实践：

`drupal-check --analysis {{path/to/directory}}`