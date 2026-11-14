# rustup set

> Изменять настройки `rustup`.
> Больше информации: <https://rust-lang.github.io/rustup/>.

- Установить тройку хоста по умолчанию:

`rustup set default-host {{тройка_хоста}}`

- Установить профиль по умолчанию (`minimal` включает только `rustc`, `rust-std` и `cargo`, тогда как `default` добавляет `rust-docs`, `rustfmt` и `clippy`):

`rustup set profile {{minimal|default}}`

- Указать, должен ли `rustup` обновлять себя при выполнении `rustup update`:

`rustup set auto-self-update {{enable|disable|check-only}}`
