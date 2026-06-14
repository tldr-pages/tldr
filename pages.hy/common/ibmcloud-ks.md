# ibmcloud ks

> Կառավարեք Kubernetes և OpenShift կլաստերները IBM Cloud-ում:.
> Լրացուցիչ տեղեկություններ. <https://cloud.ibm.com/docs/cli?topic=cli-kubernetes-service-cli>:.

- Դիտեք կլաստերի մանրամասները.:

`ibmcloud ks cluster get {{[-c|--cluster]}} {{cluster_id}}`

- Դիտեք կլաստերի մարմնի վկայագրերի ռոտացիայի կարգավիճակը.:

`ibmcloud ks cluster ca status {{[-c|--cluster]}} {{cluster_id}}`

- Դիտեք կլաստերի աշխատողների լողավազանները.:

`ibmcloud ks worker-pool ls {{[-c|--cluster]}} {{cluster_id}}`

- Ջնջեք աշխատող հանգույցը և փոխարինեք այն նորով նույն աշխատողների լողավազանում.:

`ibmcloud ks worker replace {{[-c|--cluster]}} {{cluster_id}} {{[-w|--worker]}} {{worker_id}}`

- Թվարկեք այս հրամանի ներքո հասանելի բոլոր գործողությունները.:

`ibmcloud ks help`
