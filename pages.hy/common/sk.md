# սկ

> Մշուշոտ որոնիչ, որը գրված է Rust-ով:.
> Նման `fzf`-ին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/skim-rs/skim>:.

- Սկսեք `skim`-ը նշված գրացուցակի բոլոր ֆայլերի վրա.:

`find {{path/to/directory}} -type f | sk`

- Գործընթացների գործարկման համար գործարկեք `skim`.:

`ps aux | sk`

- Սկսեք `skim`-ը նշված հարցումով.:

`sk --query "{{query}}"`

- Ընտրեք մի քանի ֆայլ `<Shift Tab>`-ով և գրեք ֆայլում՝:

`find {{path/to/directory}} -type f | sk --multi > {{path/to/file}}`
