# ananicy-cpp

> Feature-rich C++ rewrite of the Ananicy auto-nice daemon for Linux.
> More information: <https://gitlab.com/ananicy-cpp/ananicy-cpp/README.md>.

- Output all currently parsed rules and rule files:

`ananicy-cpp dump rules`

- Output all configured process types:

`ananicy-cpp dump types`

- Output all current rules in JSON format:

`ananicy-cpp dump rules --json`

- Parse and validate custom rule files without applying them:

`ananicy-cpp parse {{path/to/rules.rules}}`
