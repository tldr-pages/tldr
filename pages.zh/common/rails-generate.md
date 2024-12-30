# rails 生成

> 在现有项目中生成新的 Rails 模板。
> 更多信息：<https://guides.rubyonrails.org/command_line.html#bin-rails-generate>。

- 列出所有可用的生成器：

`rails generate`

- 生成一个名为 Post 的新模型，属性为 title 和 body：

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- 生成一个名为 Posts 的新控制器，包含操作 index、show、new 和 create：

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- 生成一个新的迁移，将 category 属性添加到名为 Post 的现有模型中：

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- 为名为 Post 的模型生成一个脚手架，预定义属性 title 和 body：

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`