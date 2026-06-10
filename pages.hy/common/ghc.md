# ghc

> Glasgow Haskell Compiler-ը:.
> Կազմում և կապում է Haskell աղբյուրի ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://downloads.haskell.org/ghc/latest/docs/users_guide/usage.html>:.

- Գտեք և կազմեք բոլոր մոդուլները ընթացիկ գրացուցակում.:

`ghc Main`

- Կազմել մեկ ֆայլ.:

`ghc {{path/to/file.hs}}`

- Կազմել՝ օգտագործելով լրացուցիչ օպտիմալացում.:

`ghc -O {{path/to/file.hs}}`

- Դադարեցրեք կոմպիլյացիան օբյեկտի ֆայլեր ստեղծելուց հետո (.o):

`ghc -c {{path/to/file.hs}}`

- Սկսեք REPL (ինտերակտիվ կեղև).:

`ghci`

- Գնահատեք մեկ արտահայտություն.:

`ghc -e {{expression}}`
