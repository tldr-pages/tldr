# nsenter

> Executați o comandă nouă în spațiul de nume al unui proces de execuție.
> Deosebit de util pentru imaginile docker sau închisorile chroot.
> Mai multe informaţii: <https://github.com/jpetazzo/nsenter/>

- Rulați comanda în procesele existente spațiu de nume de rețea:

`nsenter -t {{pid}} -n {{command}} {{command_arguments}}`

- Rulați o comandă nouă într-un spațiu de nume de masă existent procese ps-tabel:

`nsenter -t {{pid}} -p {{command}} {{command_arguments}}`

- Executați comanda în procesele existente IPC namespace:

`nsenter -t {{pid}} -i {{command}} {{command_arguments}}`
