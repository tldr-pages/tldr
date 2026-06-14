# gcloud կոնտեյներ

> Կառավարեք բեռնարկղային հավելվածները Kubernetes-ում և կլաստերներում:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/container>:.

- Գրանցեք `gcloud` որպես Docker-ի հավատարմագրերի օգնական.:

`gcloud auth configure-docker`

- Ստեղծեք կլաստեր GKE բեռնարկղերը գործարկելու համար.:

`gcloud container clusters create {{cluster_name}}`

- Թվարկեք կլաստերները GKE բեռնարկղերի գործարկման համար.:

`gcloud container clusters list`

- Թարմացրեք kubeconfig-ը՝ `kubectl` ստանալու համար՝ GKE կլաստեր օգտագործելու համար:

`gcloud container clusters get-credentials {{cluster_name}}`

- Ցուցակեք պիտակները և վերլուծեք մետատվյալները կոնտեյների պատկերի համար.:

`gcloud container images list-tags {{image}}`

- Նկարագրեք գոյություն ունեցող կլաստերը բեռնարկղերի գործարկման համար.:

`gcloud container clusters describe {{cluster_name}}`
