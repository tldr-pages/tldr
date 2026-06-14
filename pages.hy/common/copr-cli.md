# copr-cli

> Ինտերֆեյս Fedora-Projects copr օրինակի հետ RPM-ներ ստեղծելու և դրանք հրապարակելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/copr-cli>:.

- Ցուցադրել copr մուտք գործած օգտվողին.:

`copr-cli whoami`

- Կառուցեք տեղական հատուկ ֆայլ copr-ի վրա.:

`copr-cli build {{repository}} {{path/to/spec_file}}`

- Ստուգեք կառուցումների կարգավիճակը.:

`copr-cli list-builds {{repository}}`

- Գործարկեք հատուկ ֆայլի copr կառուցումը հանրային (Git) պահոցից.:

`copr-cli buildscm {{repository}} --clone-url {{https://git.example.org/repo}} --spec {{spec_file_name}}`
