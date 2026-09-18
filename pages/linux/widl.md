# widl

> Wine Interface Definition Language (IDL) compiler: generates headers, RPC stubs, proxies, type libraries and UUID files.
> More information: <https://manned.org/widl>.

- Generate a header file from an IDL file:

`widl {{[-h]}} {{path/to/input.idl}}`

- Generate a type library:

`widl {{[-t]}} {{path/to/input.idl}}`

- Generate a client stub file:

`widl {{[-c]}} {{path/to/input.idl}}`

- Generate a server stub file:

`widl {{[-s]}} {{path/to/input.idl}}`

- Generate a UUID file:

`widl {{[-u]}} {{path/to/input.idl}}`

- Cross-compile for a 64-bit target:

`widl {{[-m64]}} {{[-h]}} {{path/to/input.idl}}`
