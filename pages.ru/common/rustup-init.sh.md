# rustup-init.sh

> Скрипт для установки `rustup` и набора инструментов Rust.
> Больше информации: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- Скачать и запустить `rustup-init` для установки `rustup` и набора инструментов Rust по умолчанию:

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s`

- Скачать и запустить `rustup-init` с передачей аргументов:

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s -- {{аргументы}}`

- Запустить `rustup-init` с указанием дополнительных компонентов или целевых платформ:

`rustup-init.sh --target {{целевая_платформа}} --component {{компонент}}`

- Запустить `rustup-init` с указанием набора инструментов по умолчанию:

`rustup-init.sh --default-toolchain {{набор_инструментов}}`

- Запустить `rustup-init` без установки набора инструментов:

`rustup-init.sh --default-toolchain {{none}}`

- Запустить `rustup-init` с указанием профиля установки:

`rustup-init.sh --profile {{minimal|default|complete}}`

- Запустить `rustup-init` без запроса подтверждения:

`rustup-init.sh -y`
