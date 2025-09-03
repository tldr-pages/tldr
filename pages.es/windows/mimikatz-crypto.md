# mimikatz crypto

> Manipula los servicios criptográficos y certificados de Windows.
> Mas informacion: <https://github.com/gentilkiwi/mimikatz>.

- Listar provedores criptográficos:

`mimikatz "crypto::providers"`

- Listar claves en un proveedor criptográfico:

`mimikatz "crypto::capi"`

- Exportar certificados y claves:

`mimikatz "crypto::certificates /export"`
