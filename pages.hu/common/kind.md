# kind

> Eszköz helyi Kubernetes fürtök futtatására Docker konténer "csomópontok" segítségével. A Kubernetes tesztelésére tervezték, de használható helyi fejlesztésre vagy folyamatos integrációra is. További információ: <https://github.com/kubernetes-sigs/kind>.

- Helyi Kubernetes fürt létrehozása:

`kind create cluster --name {{cluster_name}}`

- Egy vagy több fürt törlése:

`kind delete clusters {{cluster_name}}`

- Részletek lekérdezése a fürtökről, csomópontokról vagy a kubeconfigról:

`kind get {{clusters|nodes|kubeconfig}}`

- A kubeconfig vagy a naplók exportálása:

`kind export {{kubeconfig|logs}}`
