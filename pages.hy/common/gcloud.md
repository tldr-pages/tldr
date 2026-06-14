# gcloud

> Պաշտոնական CLI գործիք Google Cloud Platform-ի համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `app`-ը և `init`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud>:.

- Թվարկեք բոլոր հատկությունները մեկի ակտիվ կազմաձևում.:

`gcloud config list`

- Մուտք գործեք Google հաշիվ.:

`gcloud auth login`

- Սահմանեք ակտիվ նախագիծը.:

`gcloud config set project {{project_name}}`

- SSH վիրտուալ մեքենայի օրինակում.:

`gcloud compute ssh {{user}}@{{instance}}`

- Ցուցադրել Google Compute Engine-ի բոլոր օրինակները նախագծում (ըստ լռելյայն օրինակները նշված են բոլոր գոտիներից).:

`gcloud compute instances list`

- Թարմացրեք kubeconfig ֆայլը համապատասխան հավատարմագրերով՝ `kubectl`-ը Google Kubernetes Engine-ի (GKE) որոշակի կլաստերի վրա ուղղելու համար:

`gcloud container clusters get-credentials {{cluster_name}}`

- Թարմացրեք բոլոր `gcloud` բաղադրիչները՝:

`gcloud components update`

- Ցուցադրել օգնություն տրված հրամանի համար.:

`gcloud help {{command}}`
