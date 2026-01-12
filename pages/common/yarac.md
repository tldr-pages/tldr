# yarac

> Compile YARA rule source files into a binary format for faster loading.
> See also: `yara`.
> More information: <https://manned.org/man/yarac>.

- Compile a specific rule file:

`yarac {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Compile multiple rule files into a single binary:

`yarac {{path/to/rule1.yar path/to/rule2.yar ...}} {{path/to/rules.bin}}`

- Define an external variable during compilation:

`yarac -d {{identifier}}={{value}} {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Disable warnings during compilation:

`yarac {{[-w|--no-warnings]}} {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Fail compilation on any warnings (do not use along with `--no-warnings`):

`yarac --fail-on-warnings {{path/to/rule.yar}} {{path/to/rule.bin}}`
