# git ls-tree

> Թվարկե՛ք ծառի օբյեկտի բովանդակությունը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-ls-tree>:.

- Թվարկե՛ք ծառի բովանդակությունը ճյուղի վրա.:

`git ls-tree {{branch_name}}`

- Թվարկե՛ք ծառի բովանդակությունը կոմմիթի վրա՝ կրկնելով ենթածառերի.:

`git ls-tree -r {{commit_hash}}`

- Թվարկեք միայն ծառի ֆայլերի անունները կոմմիթի վրա.:

`git ls-tree --name-only {{commit_hash}}`

- Տպեք ընթացիկ ճյուղի գլխի ֆայլերի անունները ծառի կառուցվածքում (Նշում. `tree --fromfile`-ը չի ապահովվում Windows-ում).:

`git ls-tree -r --name-only HEAD | tree --fromfile`
