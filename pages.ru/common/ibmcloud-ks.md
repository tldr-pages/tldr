# ibmcloud ks

> Управлять кластерами Kubernetes и OpenShift в IBM Cloud.
> Больше информации: <https://cloud.ibm.com/docs/containers?topic=containers-kubernetes-service-cli>.

- Показать подробную информацию о кластере:

`ibmcloud ks cluster get {{[-c|--cluster]}} {{идентификатор_кластера}}`

- Показать статус ротации сертификатов центра сертификации для кластера:

`ibmcloud ks cluster ca status {{[-c|--cluster]}} {{идентификатор_кластера}}`

- Показать пулы рабочих узлов кластера:

`ibmcloud ks worker-pool ls {{[-c|--cluster]}} {{идентификатор_кластера}}`

- Удалить рабочий узел и заменить его новым в том же пуле:

`ibmcloud ks worker replace {{[-c|--cluster]}} {{идентификатор_кластера}} {{[-w|--worker]}} {{идентификатор_узла}}`

- Показать все доступные действия для данной команды:

`ibmcloud ks help`
