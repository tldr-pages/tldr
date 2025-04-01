# rails generate

> 生成现有项目中的新 Rails 模板。
> 更多信息：<https://guides.rubyonrails.org/command_line.html#bin-rails-generate>。

- 列出所有可用的生成器：

`rails generate`

- 生成一个名为 Post 的新模型，包含 title 和 body 属性：

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- 生成一个名为 Posts 的新控制器，包含 index、show、new 和 create 动作：

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- 生成一个新迁移，为现有的 Post 模型添加 category 属性：

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- 为一个名为 Post 的模型生成一个脚手架，预定义 title 和 body 属性：

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`