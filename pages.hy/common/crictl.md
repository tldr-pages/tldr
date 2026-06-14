# crictl

> Կառավարեք CRI-ի հետ համատեղելի կոնտեյների գործարկման ժամանակները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>:.

- Թվարկեք բոլոր Kubernetes pods (Ready և NotReady):

`crictl pods`

- Թվարկեք բոլոր բեռնարկղերը (վազում և ելք).:

`crictl ps {{[-a|--all]}}`

- Թվարկեք բոլոր պատկերները.:

`crictl images`

- Տպել տեղեկատվություն կոնկրետ բեռնարկղերի մասին.:

`crictl inspect {{container_id1 container_id2 ...}}`

- Բացեք հատուկ կեղև հոսող կոնտեյների ներսում.:

`crictl exec {{[-it|--interactive --tty]}} {{container_id}} {{sh}}`

- Քաշեք կոնկրետ պատկեր գրանցամատյանից.:

`crictl pull {{image:tag}}`

- Տպեք և հետևեք որոշակի կոնտեյների տեղեկամատյաններին.:

`crictl logs {{[-f|--follow]}} {{container_id}}`

- Հեռացրեք մեկ կամ մի քանի պատկեր.:

`crictl rmi {{image_id1 image_id2 ...}}`
