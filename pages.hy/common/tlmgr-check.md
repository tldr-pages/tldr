# tlmgr ստուգում

> Ստուգեք TeX Live տեղադրման հետևողականությունը:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#check-option...-depends-executes-files-runfiles-texmfdbs-all>:.

- Ստուգեք ամբողջ TeX Live տեղադրման հետևողականությունը.:

`tlmgr check all`

- Ստուգեք ամբողջ TeX Live տեղեկատվության հետևողականությունը բառացի ռեժիմում.:

`tlmgr check all -v`

- Ստուգեք բացակայող կախվածությունները.:

`tlmgr check depends`

- Ստուգեք, արդյոք առկա են բոլոր TeX Live գործարկվողները.:

`tlmgr check executes`

- Ստուգեք, արդյոք առկա են տեղական TLPDB-ում թվարկված բոլոր ֆայլերը.:

`tlmgr check files`

- Ստուգեք կրկնօրինակ ֆայլերի անունները runfiles բաժիններում.:

`tlmgr check runfiles`
