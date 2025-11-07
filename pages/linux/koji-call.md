# koji call

> Execute an arbitrary XML-RPC call
> eg: build function declaration is build(src, target, opts=None, priority=None, channel=None)
> More information: <https://koji.fedoraproject.org/koji/api>.

- Call build function with scratch option:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"scratch": True}}'`

- Call build function with arch_override option:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"arch_override":"sw_64"}}'`

- Call build function on `default` channel:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"channel":"default"}'`

- Display help:

`koji call --help`
