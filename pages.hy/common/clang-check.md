# cang-check

> Ստուգեք հիմնական սխալները և աշխատեք Clang's Abstract Syntax Tree (AST) հետ:.
> Clang's LibTooling-ի մի մասն է և օգտակար է վրիպազերծման և C/C++ կոդը վերլուծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/clang-check>:.

- Գործարկել լռելյայն ստուգումները աղբյուրի ֆայլի վրա.:

`clang-check {{path/to/file.cpp}} --`

- Թափել վերացական շարահյուսական ծառը վրիպազերծման համար.:

`clang-check {{path/to/file.cpp}} -ast-dump --`

- Զտել AST անունով:

`clang-check {{path/to/file.cpp}} -ast-dump -ast-dump-filter FunctionName`

- Pretty-Print AST:

`clang-check {{path/to/file.cpp}} -ast-print --`
