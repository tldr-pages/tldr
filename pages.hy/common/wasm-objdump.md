# wasm-objdump

> Ցուցադրել տեղեկատվությունը WebAssembly երկուական սարքերից:.
> Լրացուցիչ տեղեկություններ. <https://webassembly.github.io/wabt/doc/wasm-objdump.1.html>:.

- Ցուցադրել տվյալ երկուականի բաժինների վերնագրերը.:

`wasm-objdump {{[-h|--headers]}} {{file.wasm}}`

- Ցուցադրել տվյալ երկուականի ամբողջ ապամոնտաժված ելքը.:

`wasm-objdump {{[-d|--disassemble]}} {{file.wasm}}`

- Ցուցադրել յուրաքանչյուր բաժնի մանրամասները.:

`wasm-objdump {{[-x|--details]}} {{file.wasm}}`

- Ցուցադրել տվյալ բաժնի մանրամասները.:

`wasm-objdump {{[-j|--section]}} '{{import}}' {{[-x|--details]}} {{file.wasm}}`
