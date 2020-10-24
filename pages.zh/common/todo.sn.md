# sn

> Mono StrongName utility for signing and verifying IL assemblies.

- Generate a new StrongNaming key:

`sn -k {{path/to/key.snk}}`

- Re-sign an assembly with the specified private key:

`sn -R {{path/to/assembly.dll}} {{path/to/keypair.snk}}`

- Show the public key of the private key that was used to sign an assembly:

`sn -T {{path/to/assembly.exe}}`

- Extract the public key to a file:

`sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}`
