# sass

> 将 SCSS 或 Sass 文件转换为 CSS。
> 更多信息：<https://sass-lang.com/documentation/cli/dart-sass>。

- 将 SCSS 或 Sass 文件转换为 CSS 并输出结果：

`sass {{inputfile.scss|inputfile.sass}}`

- 将 SCSS 或 Sass 文件转换为 CSS 并将结果保存到文件：

`sass {{inputfile.scss|inputfile.sass}} {{outputfile.css}}`

- 监视 SCSS 或 Sass 文件的更改，并输出或更新同名的 CSS 文件：

`sass --watch {{inputfile.scss|inputfile.sass}}`

- 监视 SCSS 或 Sass 文件的更改，并输出或更新指定名称的 CSS 文件：

`sass --watch {{inputfile.scss|inputfile.sass}}:{{outputfile.css}}`
