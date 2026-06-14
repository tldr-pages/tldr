# կոկիկ-կոկիկ

> LLVM-ի վրա հիմնված C/C++ լինտեր՝ ստատիկ վերլուծության միջոցով ոճի խախտումներ, սխալներ և անվտանգության թերություններ գտնելու համար:.
> Լրացուցիչ տեղեկություններ. <https://clang.llvm.org/extra/clang-tidy/>:.

- Գործարկել լռելյայն ստուգումները աղբյուրի ֆայլի վրա.:

`clang-tidy {{path/to/file.cpp}}`

- Մի կատարեք այլ ստուգումներ, բացի `cppcoreguidelines` ստուգումներից որևէ ֆայլի վրա.:

`clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- Նշեք բոլոր հասանելի ստուգումները.:

`clang-tidy -checks={{*}} -list-checks`

- Նշեք, սահմանում և ներառում է որպես կոմպիլյացիայի ընտրանքներ (`--`-ից հետո):

`clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}`
