# pip hash

> Ստուգման համար հաշվարկեք փաթեթների արխիվների հեշերը:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_hash/>:.

- Ստեղծեք հեշ փաթեթի ֆայլի համար.:

`pip hash {{path/to/package.whl}}`

- Ստեղծեք հեշ՝ օգտագործելով հատուկ ալգորիթմ.:

`pip hash {{[-a|--algorithm]}} {{sha256|sha384|sha512|...}} {{path/to/package.whl}}`

- Ստեղծեք հեշեր բազմաթիվ ֆայլերի համար.:

`pip hash {{path/to/package1.whl path/to/package2.whl ...}}`

- Ստեղծեք հեշ ներբեռնված արխիվի համար.:

`pip hash {{path/to/package.tar.gz}}`
