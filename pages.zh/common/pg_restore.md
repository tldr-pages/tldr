# pg_restore

> 从由 pg_dump 创建的归档文件恢复 PostgreSQL 数据库。
> 更多信息：<https://www.postgresql.org/docs/current/app-pgrestore.html>。

- 将归档恢复到现有数据库中：

`pg_restore -d {{db_name}} {{archive_file.dump}}`

- 与上述相同，定制用户名：

`pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}`

- 与上述相同，定制主机和端口：

`pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}`

- 列出包含在归档中的数据库对象：

`pg_restore --list {{archive_file.dump}}`

- 在创建数据库对象之前清理它们：

`pg_restore --clean -d {{db_name}} {{archive_file.dump}}`

- 使用多个作业进行恢复：

`pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}`