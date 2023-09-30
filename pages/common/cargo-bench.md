# cargo bench

> Compile and execute benchmarks.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Execute benchmarks of a package:

`cargo bench`

- Compile, but don’t run benchmarks:

`cargo bench --no-run`

- Benchmark only the specified packages:

`cargo bench --package`

- Benchmark the specified benchmark:

`cargo bench --bench`

- Benchmark with the given profile:

`cargo bench --profile`

- Benchmark all example targets:

`cargo bench --examples`

- Benchmark all binary targets:

`cargo bench --bins`

- Benchmark the package’s library:

`cargo bench --lib`
