# wasm-opt

> Օպտիմալացնել WebAssembly երկուական ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/wasm-opt>:.

- Կիրառեք լռելյայն օպտիմալացումներ և գրեք տվյալ ֆայլում.:

`wasm-opt -O {{input.wasm}} {{[-o|--output]}} {{output.wasm}}`

- Կիրառեք բոլոր օպտիմալացումները և գրեք տվյալ ֆայլում (ավելի շատ ժամանակ է պահանջում, բայց օպտիմալ կոդ է ստեղծում).:

`wasm-opt -O4 {{input.wasm}} {{[-o|--output]}} {{output.wasm}}`

- Օպտիմալացնել ֆայլը չափի համար.:

`wasm-opt -Oz {{input.wasm}} {{[-o|--output]}} {{output.wasm}}`

- Տպեք երկուականի տեքստային ներկայացումը մխիթարել.:

`wasm-opt {{input.wasm}} --print`
