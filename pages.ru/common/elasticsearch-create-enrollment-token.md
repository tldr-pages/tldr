# elasticsearch-create-enrollment-token

> Создавать токены регистрации для узлов Elasticsearch и экземпляров Kibana.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/create-enrollment-token>.

- Создать токен регистрации для добавления нового узла Elasticsearch:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node`

- Создать токен регистрации для добавления нового экземпляра Kibana:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana`

- Создать токен регистрации и показать подробный вывод:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node --verbose`

- Создать токен регистрации для экземпляра Kibana с пользовательским URL-адресом Elasticsearch:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana --url "{{ip_адрес}}"`

- Показать справку:

`elasticsearch-create-enrollment-token {{[-h|--help]}}`
