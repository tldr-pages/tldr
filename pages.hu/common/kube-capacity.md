# kube-capacity

> Egy egyszerű CLI, amely áttekintést nyújt az erőforrás kérésekről, korlátokról és kihasználtságról egy Kubernetes fürtben.
> A `kubectl top` és a `kubectl describe` legjobb részeinek kombinálása egy olyan CLI-ben, amely a fürt erőforrásaira összpontosít.
> További információ: <https://github.com/robscott/kube-capacity>.

- Kimeneti a csomópontok listáját a teljes CPU és Memória erőforrásigénylésekkel és korlátokkal:

`kube-capacity`

- Beleértve a podokat:

`kube-capacity -p`

- Beleértve a kihasználtságot:

`kube-capacity -u`
