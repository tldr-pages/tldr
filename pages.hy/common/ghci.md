#ղչի

> Glasgow Haskell Compiler-ի ինտերակտիվ միջավայրը:.
> Լրացուցիչ տեղեկություններ. <https://downloads.haskell.org/ghc/latest/docs/users_guide/ghci.html>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`ghci`

- Սկսեք REPL և բեռնեք նշված Haskell աղբյուրի ֆայլը.:

`ghci {{source_file.hs}}`

- Սկսեք REPL և միացրեք լեզվի տարբերակը.:

`ghci -X{{language_option}}`

- Սկսեք REPL և միացրեք կոմպիլյատորների որոշ մակարդակի նախազգուշացումներ (օրինակ՝ `all` կամ `compact`):

`ghci -W{{warning_level}}`

- Սկսեք REPL-ը երկու կետով բաժանված դիրեկտորիաների ցանկով՝ աղբյուրի ֆայլերը գտնելու համար.:

`ghci -i{{path/to/directory1:path/to/directory2:...}}`
