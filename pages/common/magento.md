# magento

> A CLI for managing the Magento PHP framework.
> More information: <https://magento.com>.

- Enable one or more space-separated modules:

`magento module:enable {{module1 module2 ...}}`

- Disable one or more space-separated modules:

`magento module:disable {{module1 module2 ...}}`

- Update the database after enabling modules:

`magento setup:upgrade`

- Update code and dependency injection configuration:

`magento setup:di:compile`

- Deploy static assets:

`magento setup:static-content:deploy`

- Enable maintenance mode:

`magento maintenance:enable`

- Disable maintenance mode:

`magento maintenance:disable`

- List all available commands:

`magento list`
