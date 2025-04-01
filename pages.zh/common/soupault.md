# soupault

> 基于 HTML 元素树重写的静态网站生成器。
> 也可以用作 HTML 后处理器或元数据提取器。
> 更多信息：<https://soupault.app>。

- 在当前工作目录中初始化一个最小的网站项目：

`soupault --init`

- 构建网站：

`soupault`

- 覆盖默认配置文件和目录位置：

`soupault --config {{config_path}} --site-dir {{input_dir}} --build-dir {{output_dir}}`

- 提取元数据到 JSON 文件中，不生成页面：

`soupault --index-only --dump-index-json {{path/to/file.json}}`

- 显示有效的配置（`soupault.toml` 中的值加上默认值）：

`soupault --show-effective-config`
