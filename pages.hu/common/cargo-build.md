# cargo build

> Egy helyi csomag és az összes függőségi csomag fordítása. További információ: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- A `Cargo.toml` manifeszt fájlban meghatározott csomag vagy csomagok összeállítása a helyi elérési útvonalon:

`cargo build`

- Leleteket építsen kiadás módban, optimalizációkkal:

`cargo build --release`

- Követelmény, hogy a `Cargo.lock` naprakész legyen:

`cargo build --locked`

- A munkaterület összes csomagjának építése:

`cargo build --workspace`

- Egy adott csomag építése:

`cargo build --package {{package}}`

- Csak a megadott bináris csomagot építse:

`cargo build --bin {{name}}`

- Csak a megadott tesztcélt építse:

`cargo build --test {{testname}}`
