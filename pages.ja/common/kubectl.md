# kubectl

> Kubernetes クラスタに対してコマンドを実行するためのコマンドラインインターフェイス。
> `run` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://kubernetes.io/docs/reference/kubectl/>。

- リソースに関する情報をより詳細に一覧表示する:

`kubectl get {{pod|service|deployment|ingress|...}} {{[-o|--output]}} wide`

- 指定したポッドにラベル 'unhealthy' と値 'true' を付けて更新する:

`kubectl label pods {{ポッド名}} unhealthy=true`

- 異なるタイプのリソースを全て一覧表示する:

`kubectl get all`

- ノードまたはポッドのリソース (CPU/Memory/Storage) 使用量を表示する:

`kubectl top {{pod|node}}`

- マスターとクラスタサービスのアドレスを表示する:

`kubectl cluster-info`

- 特定のフィールドの説明を表示する:

`kubectl explain {{pods.spec.containers}}`

- ポッドまたは指定したリソース内のコンテナのログを表示する:

`kubectl logs {{ポッド名}}`

- 既存のポッドでコマンドを実行する:

`kubectl exec {{ポッド名}} -- {{ls /}}`
