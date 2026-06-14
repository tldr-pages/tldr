# kubectl ստեղծել

> Ստեղծեք ռեսուրս ֆայլից կամ `stdin`-ից:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/>:.

- Ստեղծեք ռեսուրս՝ օգտագործելով ռեսուրսի սահմանման ֆայլը.:

`kubectl create {{[-f|--filename]}} {{path/to/file.yml}}`

- Ստեղծեք ռեսուրս `stdin`-ից՝:

`kubectl create {{[-f|--filename]}} -`

- Ստեղծեք տեղակայում.:

`kubectl create {{[deploy|deployment]}} {{deployment_name}} --image {{image}}`

- Ստեղծեք տեղակայում կրկնօրինակներով.:

`kubectl create {{[deploy|deployment]}} {{deployment_name}} --image {{image}} --replicas {{number_of_replicas}}`

- Ստեղծեք ծառայություն.:

`kubectl create {{[svc|service]}} {{service_type}} {{service_name}} --tcp {{port}}:{{target_port}}`

- Ստեղծեք անվանատարածք.:

`kubectl create {{[ns|namespace]}} {{namespace_name}}`
