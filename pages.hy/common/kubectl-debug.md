# kubectl վրիպազերծում

> Վրիպազերծել կլաստերի ռեսուրսները՝ օգտագործելով վրիպազերծման ինտերակտիվ կոնտեյներներ:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/>:.

- Ստեղծեք ինտերակտիվ վրիպազերծման նիստ պատիճում և անմիջապես կցեք դրան.:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image busybox`

- Ստեղծեք վրիպազերծման կոնտեյներ հատուկ պատկերով և անունով.:

`kubectl debug --image {{image}} {{[-c|--container]}} {{container_name}} {{pod_name}}`

- Ստեղծեք ինտերակտիվ վրիպազերծման սեսիա հանգույցի վրա և անմիջապես կցեք դրան (կոնտեյները կաշխատի հյուրընկալողի անվանատարածքներում, և հյուրընկալողի ֆայլային համակարգը կտեղադրվի `/host` հասցեով):

`kubectl debug node/{{node_name}} {{[-it|--stdin --tty]}} --image busybox`

- Ստեղծեք պատի պատճեն և դրան ավելացրեք վրիպազերծման կոնտեյներ.:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image {{image}} --copy-to {{pod_copy_name}}`

- Ստեղծեք պատիճի պատճեն և փոխեք որոշակի կոնտեյների հրամանը.:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --copy-to {{pod_copy_name}} --container {{container_name}} -- {{command}}`

- Ստեղծեք պատիճի պատճեն և փոխեք որոշակի կոնտեյների պատկերը.:

`kubectl debug {{pod_name}} --copy-to {{pod_copy_name}} --set-image {{container_name}}={{image}}`

- Ստեղծեք պատիճի պատճեն և փոխեք բեռնարկղերի բոլոր պատկերները.:

`kubectl debug {{pod_name}} --copy-to {{pod_copy_name}} --set-image '*={{image}}'`

- Ստեղծեք վրիպազերծման ժամանակավոր կոնտեյներ և թիրախավորեք որոշակի կոնտեյներ (օգտակար է անգործուն բեռնարկղերը կարգաբերելու համար).:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image {{image}} --target {{target_container_name}}`
