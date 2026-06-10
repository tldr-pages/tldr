# git check-attr

> Յուրաքանչյուր ուղու անվան համար նշեք, եթե յուրաքանչյուր հատկանիշ չճշտված է, դրված կամ չսահմանված է որպես gitattribute այդ ուղու անվան վրա:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-check-attr>:.

- Ստուգեք ֆայլի բոլոր հատկանիշների արժեքները.:

`git check-attr {{[-a|--all]}} {{path/to/file}}`

- Ստուգեք որոշակի հատկանիշի արժեքը ֆայլի վրա.:

`git check-attr {{attribute}} {{path/to/file}}`

- Ստուգեք բոլոր հատկանիշների արժեքները կոնկրետ ֆայլերի վրա.:

`git check-attr {{[-a|--all]}} {{path/to/file1 path/to/file2 ...}}`

- Ստուգեք որոշակի հատկանիշի արժեքը մեկ կամ մի քանի ֆայլերի վրա.:

`git check-attr {{attribute}} {{path/to/file1 path/to/file2 ...}}`
