# ibmcloud cr

> Կառավարեք IBM Cloud Container Registry-ի բովանդակությունը և կազմաձևումը:.
> Լրացուցիչ տեղեկություններ. <https://cloud.ibm.com/docs/cli?topic=cli-containerregcli>:.

- Սահմանեք թիրախային տարածքը IBM Cloud Container Registry-ի համար.:

`ibmcloud cr region-set`

- Ցուցակեք առկա պատկերները.:

`ibmcloud cr {{[images|image-list]}}`

- Ստուգեք պատկերի տվյալները.:

`ibmcloud cr image-inspect {{image}}`

- Կատարեք խոցելիության գնահատում պատկերի վրա.:

`ibmcloud cr {{[va|vulnerability-assessment]}} {{image}}`

- Մուտք գործեք տեղական Docker կամ Podman հաճախորդը IBM Cloud Container Registry.:

`ibmcloud cr login`

- Թվարկեք այս հրամանի ներքո հասանելի բոլոր գործողությունները.:

`ibmcloud cr help`
