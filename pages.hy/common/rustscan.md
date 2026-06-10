# ժանգոտում

> Ժամանակակից Port Scanner գրված Rust-ով:.
> Նշում. `nmap`-ը պետք է տեղադրվի, որպեսզի ստորև բերված որոշ օրինակներ աշխատեն:.
> Տես նաև՝ `hping3`, `masscan`, `naabu`, `nmap`, `zmap`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bee-san/RustScan/wiki>:.

- Սկանավորեք մեկ կամ մի քանի ստորակետերով սահմանազատված հասցեների բոլոր նավահանգիստները՝ օգտագործելով լռելյայն արժեքները.:

`rustscan {{[-a|--addresses]}} {{ip_or_hostname1,ip_or_hostname2,...}}`

- Սկանավորեք լավագույն 1000 նավահանգիստները ծառայության և տարբերակի հայտնաբերման միջոցով.:

`rustscan --top {{[-a|--addresses]}} {{address}}`

- Սկանավորեք նավահանգիստների հատուկ ցուցակ.:

`rustscan {{[-p|--ports]}} {{port1,port2,...}} {{[-a|--addresses]}} {{address}}`

- Սկանավորեք նավահանգիստների որոշակի շրջանակ.:

`rustscan {{[-r|--range]}} {{start}}-{{end}} {{[-a|--addresses]}} {{address}}`

- Հրավիրեք `nmap` գործառույթները (Nmap-ի ՕՀ-ի հայտնաբերումը և լռելյայն սկրիպտները).:

`rustscan {{[-a|--addresses]}} {{address}} -- -O {{[-sC|--script=default]}}`

- Սկանավորել հատուկ խմբաքանակի չափով (կանխադրված՝ 4500) և ժամանակի դադար (կանխադրված՝ 1500 մվ):

`rustscan {{[-b|--batch-size]}} {{batch_size}} {{[-t|--timeout]}} {{timeout}} {{[-a|--addresses]}} {{address}}`

- Սկանավորեք հատուկ նավահանգիստների պատվերով.:

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{address}}`

- Սկանավորել greppable ռեժիմով (միայն նավահանգիստների ելքը, ոչ `nmap`):

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{address}}`
