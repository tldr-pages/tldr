# rails db

> Ruby on Rails 的各种数据库相关子命令。
> 更多信息：<https://guides.rubyonrails.org/active_record_migrations.html>。

- 创建数据库，加载模式，并用初始数据初始化：

`rails db:setup`

- 访问数据库控制台：

`rails db`

- 创建当前环境定义的数据库：

`rails db:create`

- 删除当前环境定义的数据库：

`rails db:drop`

- 运行待处理的迁移：

`rails db:migrate`

- 查看每个迁移文件的状态：

`rails db:migrate:status`

- 回滚最后一个迁移：

`rails db:rollback`

- 用 `db/seeds.rb` 中定义的数据填充当前数据库：

`rails db:seed`
