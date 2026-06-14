# git verify-commit

> Ստուգեք պարտավորությունների GPG ստուգումը:.
> Եթե ոչ մի պարտավորություն չստուգվի, ոչինչ չի տպվի՝ անկախ նշված տարբերակներից:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-verify-commit>:.

- Ստուգեք պարտավորությունները GPG ստորագրության համար.:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}}`

- Ստուգեք պարտավորությունները GPG ստորագրության համար և ցույց տվեք յուրաքանչյուր պարտավորության մանրամասները.:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} {{[-v|--verbose]}}`

- Ստուգեք պարտավորությունները GPG ստորագրության համար և տպեք չմշակված մանրամասները.:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw`
