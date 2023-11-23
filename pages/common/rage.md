# rage

> A simple, secure and modern file encryption tool (and Rust library) with small explicit keys, no config options, and UNIX-style composability.
> Rust implementation of `age`.
> More information: <https://github.com/str4d/rage>.

- Encrypt a file for `user` and save it to `message.age`:

`echo "{{Your secret message}}" | rage --encrypt --recipient {{user}} --output {{path/to/message.age}}`

- Decrypt a file with `identity_file` and save it to `message`:

`rage --decrypt --identity {{path/to/identity_file}} --output {{message}}`
