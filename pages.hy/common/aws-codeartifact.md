# aws կոդի արտեֆակտ

> Կառավարեք CodeArtifact-ի պահոցները, տիրույթները, փաթեթները, փաթեթի տարբերակները և ակտիվները:.
> CodeArtifact-ը արտեֆակտի պահոց է, որը համատեղելի է հանրաճանաչ փաթեթների կառավարիչների հետ և ստեղծել գործիքներ, ինչպիսիք են Maven, Gradle, npm, Yarn, Twine, pip, NuGet և SwiftPM:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/codeartifact/>:.

- Թվարկեք հասանելի տիրույթները ձեր AWS հաշվի համար.:

`aws codeartifact list-domains`

- Ստեղծեք հավատարմագրեր որոշակի փաթեթի կառավարչի համար.:

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{your_domain}} --repository {{repository_name}}`

- Ստացեք CodeArtifact պահեստի վերջնակետի URL-ը.:

`aws codeartifact get-repository-endpoint --domain {{your_domain}} --repository {{repository_name}} --format {{npm|pypi|maven|nuget|generic}}`

- Ցուցադրել օգնությունը.:

`aws codeartifact help`

- Ցուցադրել օգնություն կոնկրետ ենթահրամանի համար.:

`aws codeartifact {{subcommand}} help`
