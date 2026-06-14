# cs լուծում

> Resolve-ը թվարկում է այլ կախվածությունների անցումային կախվածությունները:.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-resolve>:.

- Լուծել երկու կախվածությունների անցումային կախվածությունների ցուցակները.:

`cs resolve {{group_id1}}:{{artifact_id1}}:{{artifact_version1}} {{group_id2}}:{{artifact_id2}}:{{artifact_version2}}`

- Փաթեթի անցումային կախվածությունների ցուցակները լուծեք կախվածության ծառով.:

`cs resolve --tree {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Կախվածության ծառը լուծեք հակառակ հերթականությամբ (կախվածությունից դեպի իր կախվածությունը).:

`cs resolve --reverse-tree {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Տպել բոլոր գրադարանները, որոնք կախված են որոշակի գրադարանից.:

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}`

- Տպեք բոլոր գրադարանները, որոնք կախված են գրադարանի որոշակի տարբերակից.:

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}{{searched_artifact_version}}`

- Տպել հնարավոր կոնֆլիկտները մի շարք փաթեթների միջև.:

`cs resolve --conflicts {{group_id1:artifact_id1:artifact_version1 group_id2:artifact_id2:artifact_version2 ...}}`
