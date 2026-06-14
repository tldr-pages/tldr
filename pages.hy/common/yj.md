# yj

> Փոխակերպեք YAML, TOML, JSON և HCL միջև՝ պահպանելով քարտեզի կարգը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sclevine/yj>:.

- Փոխարկեք [y]AML-ը JSON-ի (կանխադրված) `stdin`-ից և արդյունքը գրեք `stdout`-ի:

`yj < {{file.yml}} -y`

- Փոխարկել [t]OML-ը [y]AML:

`yj < {{file.toml}} -ty`

- Փոխարկեք [j]SON-ը [t]OML-ի [i]նշվածությամբ.:

`yj < {{file.json}} -jti`

- Փոխարկել H[c]L-ը [j]SON:

`yj < {{file.hcl}} -cj`

- Փոխարկել [y]AML-ի H[c]L՝ անտեսելով inf/[n]aN փոխակերպումը.:

`yj < {{file.yml}} -ycn`

- Ցուցադրել [v]տարբերակ.:

`yj -v`
