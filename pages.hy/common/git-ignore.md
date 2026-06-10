# git անտեսել

> Ցույց տալ/թարմացնել `.gitignore` ֆայլերը:.
> `git-extras`-ի մի մասը:.
> Տես նաև՝ `git ignore-io`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-ignore>:.

- Ցույց տալ բոլոր գլոբալ և տեղական `.gitignore` ֆայլերի բովանդակությունը.:

`git ignore`

- Անտեսել ֆայլ(ներ)ը մասնավոր՝ թարմացնելով `.git/info/exclude` ֆայլը՝:

`git ignore {{file_pattern}} {{[-p|--private]}}`

- Անտեսել ֆայլ(ներ)ը տեղայնորեն՝ թարմացնելով տեղական `.gitignore` ֆայլը՝:

`git ignore {{file_pattern}}`

- Անտեսել ֆայլ(ներ)ը գլոբալ՝ թարմացնելով գլոբալ `.gitignore` ֆայլը՝:

`git ignore {{file_pattern}} {{[-g|--global]}}`
