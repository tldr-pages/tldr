# cargo report

> Display various kinds of reports.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-report.html>.

- Display a report of crates which will eventually stop compiling:

`cargo report future-incompatibilities`

- Display a report with the specified Cargo-generated ID:

`cargo report future-incompatibilities --id {{id}}`

- Display a report for the specified package:

`cargo report future-incompatibilities {{[-p|--package]}} {{package}}`
