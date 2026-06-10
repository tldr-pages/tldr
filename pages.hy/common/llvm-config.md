# llvm-config

> Ստացեք տարբեր կոնֆիգուրացիայի տեղեկություններ, որոնք անհրաժեշտ են LLVM օգտագործող ծրագրեր կազմելու համար:.
> Սովորաբար կանչվում է build համակարգերից, օրինակ՝ Makefiles-ում կամ կարգավորելու սկրիպտներում:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/llvm-config.html>:.

- Կազմել և կապել LLVM-ի վրա հիմնված ծրագիր.:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{path/to/output_executable}} {{path/to/source.cc}}`

- Տպեք ձեր LLVM տեղադրման `PREFIX`-ը.:

`llvm-config --prefix`

- Տպեք ձեր LLVM կառուցվածքի կողմից աջակցվող բոլոր թիրախները.:

`llvm-config --targets-built`
