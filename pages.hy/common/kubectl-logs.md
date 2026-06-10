# kubectl տեղեկամատյաններ

> Ցուցադրել տարաների տեղեկամատյանները պատիճում:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/>:.

- Ցուցադրել տեղեկամատյանները մեկ կոնտեյներով պատիճի համար.:

`kubectl logs {{pod_name}}`

- Ցույց տալ տեղեկամատյանները նշված կոնտեյների համար պատիճում.:

`kubectl logs {{[-c|--container]}} {{container_name}} {{pod_name}}`

- Ցուցադրել տեղեկամատյանները պատիճում գտնվող բոլոր բեռնարկղերի համար.:

`kubectl logs --all-containers={{true}} {{pod_name}}`

- Հոսքի պատիճ տեղեկամատյաններ.:

`kubectl logs {{[-f|--follow]}} {{pod_name}}`

- Ցուցադրել մատյանները ավելի նոր, քան հարաբերական ժամանակն է, օրինակ՝ `10s`, `5m` կամ `1h`:

`kubectl logs --since {{relative_time}} {{pod_name}}`

- Ցույց տալ 10 ամենավերջին տեղեկամատյանները պատիճում.:

`kubectl logs --tail {{10}} {{pod_name}}`

- Ցույց տալ բոլոր տեղեկամատյանները տվյալ տեղակայման համար.:

`kubectl logs {{[deploy|deployment]}}/{{deployment_name}}`
