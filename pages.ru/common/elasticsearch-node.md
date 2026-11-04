# elasticsearch-node

> Управлять низкоуровневыми операциями узла Elasticsearch, такими как завершение работы, переназначение роли или просмотр информации.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/node-tool>.

- Показать информацию о текущем узле:

`elasticsearch-node info`

- Подготовить узел к полной перезагрузке кластера (например, после обновления):

`elasticsearch-node unsafe-bootstrap`

- Переназначить роль узла (например, с master на data):

`elasticsearch-node repurpose`

- Вывести список ролей, назначенных узлу:

`elasticsearch-node roles`

- Показать установленную версию JVM, путь к домашнему каталогу Elasticsearch и другую диагностическую информацию:

`elasticsearch-node diagnostics`

- Показать справку:

`elasticsearch-node {{[-h|--help]}}`
