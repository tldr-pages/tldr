# Projucer

> JUCE 框架应用程序的项目管理器。
> 更多信息：<https://juce.com/discover/stories/projucer-manual#10.4-command-line-tools>.

- 显示项目信息：

`Projucer --status {{path/to/project_file}}`

- 重新保存项目中的所有文件和资源：

`Projucer --resave {{path/to/project_file}}`

- 更新项目中的版本号：

`Projucer --set-version {{version_number}} {{path/to/project_file}}`

- 从 PIP 文件生成 JUCE 项目：

`Projucer --create-project-from-pip {{path/to/PIP}} {{path/to/output}}`

- 移除所有 JUCE 风格的注释 (`//=====`, `//-----` 或 `///////`)：

`Projucer --tidy-divider-comments {{path/to/target_folder}}`

- 显示帮助：

`Projucer --help`
