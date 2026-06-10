#կոմակ

> Ստեղծեք WinGet մանիֆեստներ `winget-pkgs` պահոցի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/russellbanks/Komac>:.

- Ստեղծեք նոր փաթեթ զրոյից.:

`komac new {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Թարմացրեք առկա փաթեթը նոր տարբերակով.:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Թարմացրեք փաթեթը բազմաթիվ URL-ներով և ինքնաբերաբար ներկայացրեք.:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe https://example.com/app.msi ...}} {{[-s|--submit]}}`

- Հեռացրեք տարբերակը winget-pkgs-ից.:

`komac remove {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}}`

- Թվարկեք փաթեթի բոլոր տարբերակները.:

`komac {{[list|list-versions]}} {{Package.Identifier}}`

- Համաժամացրեք winget-pkgs-ի ձեր պատառաքաղը վերին հոսքի պահոցի հետ.:

`komac {{[sync|sync-fork]}}`

- Թարմացրեք պահված GitHub նշանը.:

`komac token {{[add|update]}} {{[-t|--token]}} {{your_github_token}}`

- Ստեղծեք կեղևի ավտոմատ լրացման սցենար.:

`komac {{[complete|autocomplete]}} {{bash|elvish|fish|powershell|zsh}}`
