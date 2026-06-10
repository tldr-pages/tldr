#լուալատեքս

> TeX-ի ընդլայնված տարբերակը՝ օգտագործելով Lua-ն կոմպիլյացիայի համար:.
> Լրացուցիչ տեղեկություններ. <https://texdoc.org/serve/tex.man1.pdf/0>:.

- Սկսեք `texlua`-ը՝ որպես Լուա թարգմանիչ՝:

`lualatex`

- Կազմեք Tex ֆայլ PDF-ում.:

`lualatex {{path/to/file.tex}}`

- Կազմեք Tex ֆայլ առանց սխալի ընդհատման.:

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- Կազմեք Tex ֆայլ հատուկ ելքային ֆայլի անունով.:

`lualatex -jobname={{filename}} {{path/to/file.tex}}`
