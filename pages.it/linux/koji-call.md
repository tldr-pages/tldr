# koji call

> Esegue una chiamata XML-RPC arbitraria.
> Es: la dichiarazione della funzione build è build(src, target, opts=None, priority=None, channel=None).
> Maggiori informazioni: <https://koji.fedoraproject.org/koji/api>.

- Chiama la funzione build con opzione scratch:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"scratch": True}}'`

- Chiama la funzione build con opzione arch_override:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"arch_override":"sw_64"}}'`

- Chiama la funzione build sul canale `default`:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"channel":"default"}'`

- Mostra aiuto:

`koji call {{[-h|--help]}}`
