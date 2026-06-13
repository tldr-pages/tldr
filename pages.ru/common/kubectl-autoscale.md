# kubectl autoscale

> Создавать автомасштабировщик для интеллектуального масштабирования количества подов на основе потребностей кластера Kubernetes.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/>.

- Настроить автомасштабирование развёртывания без указания целевой загрузки CPU:

`kubectl autoscale {{[deploy|deployment]}} {{имя_развёртывания}} --min {{мин_реплик}} --max {{макс_реплик}}`

- Настроить автомасштабирование развёртывания с целевой загрузкой CPU:

`kubectl autoscale {{[deploy|deployment]}} {{имя_развёртывания}} --max {{макс_реплик}} --cpu-percent {{целевой_cpu}}`
