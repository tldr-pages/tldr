# kubectl port-forward

> Փոխանցել մեկ կամ մի քանի տեղական նավահանգիստներ դեպի պատիճ:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/>:.

- Փոխանցել տեղական 5000 և 6000 նավահանգիստները դեպի pod նավահանգիստներ 5000 և 6000:

`kubectl port-forward {{[po|pods]}}/{{pod_name}} 5000 6000`

- Պատահական տեղական նավահանգիստ փոխանցեք դեպի pod նավահանգիստ 5000:

`kubectl port-forward {{[po|pods]}}/{{pod_name}} :5000`

- Փոխանցել տեղական 5000 և 6000 նավահանգիստները տեղակայման 5000 և 6000 նավահանգիստներին.:

`kubectl port-forward {{[deploy|deployment]}}/{{deployment_name}} 5000 6000`

- Փոխանցեք տեղական 8443 նավահանգիստը դեպի https անունով սպասարկման նավահանգիստ:

`kubectl port-forward {{[svc|service]}}/{{service_name}} 8443:https`

- Փոխանցել 8888 նավահանգիստը բոլոր հասցեների վրա դեպի pod նավահանգիստ 5000:

`kubectl port-forward {{[po|pods]}}/{{pod_name}} 8888:5000 --address 0.0.0.0`

- Փոխանցեք 8888 նավահանգիստը localhost-ի վրա և ընտրված IP-ն դեպի pod նավահանգիստ 5000:

`kubectl port-forward {{[po|pods]}}/{{pod_name}} 8888:5000 --address localhost,{{10.19.21.23}}`
