#ընտրել

> Գործարկեք օպտիմալացումներ և վերլուծեք LLVM աղբյուրի ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/opt.html>:.

- Գործարկեք օպտիմիզացում կամ վերլուծություն բիթկոդի ֆայլի վրա.:

`opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- Արտադրեք ֆունկցիայի վերահսկման հոսքի գրաֆիկը `.dot` ֆայլ.:

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- Օպտիմիզացրեք ծրագիրը 2-րդ մակարդակում և ստացեք արդյունքը մեկ այլ ֆայլ.:

`opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}`
