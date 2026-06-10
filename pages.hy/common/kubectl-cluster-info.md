# kubectl կլաստեր-ինֆորմացիա

> Ցուցադրել վերջնակետի մասին տեղեկությունները Kubernetes-ի վարպետի և կլաստերի ծառայությունների մասին:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/>:.

- Ցույց տալ հիմնական կլաստերի տեղեկատվությունը.:

`kubectl cluster-info`

- Ընթացիկ կլաստերի վիճակը տեղափոխել `stdout` (վրիպազերծման համար).:

`kubectl cluster-info dump`

- Կլաստերի վիճակն ուղարկել գրացուցակ.:

`kubectl cluster-info dump --output-directory {{path/to/directory}}`

- Օգտագործեք հատուկ kubeconfig համատեքստ.:

`kubectl cluster-info --context {{context_name}}`
