# bluebuild

> 基于您的 `recipe.yml` 构建 Containerfiles 和自定义镜像。
> 更多信息：<https://github.com/blue-build/cli>.

- 构建一个配方：

`bluebuild build {{path/to/recipe.yml}}`

- 验证一个配方：

`bluebuild validate {{path/to/recipe.yml}}`

- 生成一个 Containerfile：

`bluebuild generate --output {{Containerfile}} {{path/to/recipe.yml}}`

- 从配方生成 ISO：

`bluebuild generate-iso --output-dir {{path/to/output_directory}} --iso-name {{iso_name.iso}} recipe {{path/to/recipe.yml}}`

- 显示帮助：

`bluebuild --help`