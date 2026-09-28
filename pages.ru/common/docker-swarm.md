# docker swarm

> Инструмент оркестрации контейнеров.
> Больше информации: <https://docs.docker.com/engine/swarm/>.

- Инициализировать кластер swarm:

`docker swarm init`

- Показать токен для присоединения менеджера или воркера:

`docker swarm join-token {{worker|manager}}`

- Присоединить новый узел к кластеру:

`docker swarm join --token {{токен}} {{url_узла_менеджера:2377}}`

- Удалить воркер из swarm (выполнить внутри узла воркера):

`docker swarm leave`

- Показать текущий сертификат CA в формате PEM:

`docker swarm ca`

- Ротировать текущий сертификат CA и показать новый сертификат:

`docker swarm ca --rotate`

- Изменить срок действия сертификатов узлов:

`docker swarm update --cert-expiry {{часы}}h{{минуты}}m{{секунды}}s`
