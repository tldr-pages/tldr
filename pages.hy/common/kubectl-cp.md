# kubectl cp

> Պատճենեք ֆայլերը և գրացուցակները տեղական ֆայլային համակարգի և կոնտեյների միջև՝ պատիճում:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/>:.

- Պատճենեք տեղական ֆայլը կամ գրացուցակը պատիճ.:

`kubectl cp {{path/to/local_file}} {{pod_name}}:/{{path/to/file_in_pod}}`

- Պատճենեք տեղական ֆայլը կամ գրացուցակը հատուկ անվանական տարածքում գտնվող պատիճ.:

`kubectl cp {{path/to/local_file}} {{namespace}}/{{pod_name}}:/{{path/to/file_in_pod}}`

- Պատճենեք ֆայլը կամ գրացուցակը պատիճից տեղական մեքենա.:

`kubectl cp {{namespace}}/{{pod_name}}:/{{path/to/file_in_pod}} {{path/to/local_file}}`

- Պատճենեք ֆայլը կամ գրացուցակը հատուկ կոնտեյների մեջ՝ պատիճ.:

`kubectl cp {{path/to/local_file}} {{pod_name}}:/{{path/to/file_in_pod}} {{[-c|--container]}} {{container_name}}`

- Պատճենեք ֆայլը կամ գրացուցակը պատիճ առանց սեփականության և թույլտվությունների պահպանման.:

`kubectl cp {{path/to/local_file}} {{namespace}}/{{pod_name}}:/{{path/to/file_in_pod}} --no-preserve`

- Պատճենեք տեղական ֆայլը կամ գրացուցակը մի պատիճ՝ ձախողման դեպքում կրկնվող փորձերով.:

`kubectl cp {{path/to/local_file}} {{pod_name}}:/{{path/to/file_in_pod}} --retries {{3}}`
