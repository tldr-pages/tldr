# cs ամբողջական-խոր

> Որոնեք գրադարաններ՝ առանց դա ուղղակիորեն համացանցում անելու:.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-complete>:.

- Տպեք, թե որ արտեֆակտներն են հրապարակվում Maven խմբի հատուկ նույնացուցիչի ներքո.:

`cs complete-dep {{group_id}}`

- Ցուցակեք հրատարակված գրադարանի տարբերակները հատուկ Maven խմբի նույնացուցիչի և արտեֆակտի ներքո.:

`cs complete-dep {{group_id}}:{{artifact_id}}`

- Տպեք, թե որ արտեֆակտներն են հրապարակվում տվյալ Maven groupId-ի ներքո՝ փնտրելով ivy2local-ում.:

`cs complete-dep {{group_id}} --repository ivy2local`

- Ցուցակե՛ք հրապարակված արտեֆակտները Maven խմբի նույնացուցիչի ներքո, որոնք որոնում են հատուկ պահոցում և հավատարմագրերում.:

`cs complete-dep {{group_id}}:{{artifact_id}} --repository {{repository_url}} --credentials {{user}}:{{password}}`
