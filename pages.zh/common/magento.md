# magento

> 管理 Magento PHP 框架。
> 更多信息：<https://experienceleague.adobe.com/en/docs/commerce-operations/tools/cli-reference/commerce-on-premises>.

- 启用一个或多个模块：

`magento module:enable {{module1 module2 ...}}`

- 禁用一个或多个模块：

`magento module:disable {{module1 module2 ...}}`

- 在启用模块后更新数据库：

`magento setup:upgrade`

- 更新代码和依赖注入配置：

`magento setup:di:compile`

- 部署静态资源：

`magento setup:static-content:deploy`

- 启用维护模式：

`magento maintenance:enable`

- 禁用维护模式：

`magento maintenance:disable`

- 列出所有可用命令：

`magento list`
