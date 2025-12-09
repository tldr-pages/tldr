# mimikatz crypto

> Manipula los servicios criptográficos y certificados de Windows.
> Más información: <https://github.com/gentilkiwi/mimikatz>.

- Lista proveedores criptográficos:

`mimikatz "crypto::providers"`

- Lista claves en un proveedor criptográfico:

`mimikatz "crypto::capi"`

- Exporta certificados y claves:

`mimikatz "crypto::certificates /export"`
