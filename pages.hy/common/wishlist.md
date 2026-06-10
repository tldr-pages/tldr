# ցանկությունների ցուցակ

> SSH գրացուցակ և մուլտիպլեքսոր:.
> Գործում է որպես մեկ մուտքի կետ SSH սերվերներին կամ Wish հավելվածներին միանալու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/charmbracelet/wishlist>:.

- Ուսումնասիրեք ձեր `~/.ssh/config` ֆայլում թվարկված SSH սերվերները (տեղական ռեժիմ).:

`wishlist`

- Սկսեք ցանկությունների ցանկը սերվերի ռեժիմում՝ հեռակա մուտք ապահովելու համար.:

`wishlist {{[s|serve]}}`

- Օգտագործեք հատուկ կազմաձևման ֆայլ.:

`wishlist {{[-c|--config]}} {{path/to/config.yaml}}`

- Բացահայտեք SSH վերջնակետերը՝ օգտագործելով Zeroconf (mDNS/Bonjour):

`wishlist --zeroconf.enabled`

- Բացահայտեք SSH հանգույցները DNS SRV գրառումներից.:

`wishlist --srv.domain {{example.com}}`

- Բացահայտեք SSH հանգույցները Tailscale tailnet-ից.:

`wishlist --tailscale.net={{tailnet_name}} --tailscale.key={{tskey-api-abc123}}`
