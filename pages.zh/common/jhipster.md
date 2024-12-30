# jhipster

> 使用单体或微服务架构的Web应用程序生成器。
> 更多信息：<https://www.jhipster.tech/>.

- 生成一个简单的全栈项目（单体或微服务）：

`jhipster`

- 生成一个简单的前端项目：

`jhipster --skip-server`

- 生成一个简单的后端项目：

`jhipster --skip-client`

- 将最新的JHipster更新应用到项目中：

`jhipster upgrade`

- 向生成的项目中添加一个新实体：

`jhipster entity {{entity_name}}`

- 导入JDL文件以配置您的应用程序（请参见：<https://start.jhipster.tech/jdl-studio/>）：

`jhipster import-jdl {{first_file.jh second_file.jh ... n_file.jh}}`

- 为您的应用程序生成CI/CD管道：

`jhipster ci-cd`

- 为您的应用程序生成Kubernetes配置：

`jhipster kubernetes`