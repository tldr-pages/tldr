# koji call

> اجرای فراخوانی دلخواه XML-RPC.
> مثال: اعلان تابع ساخت به‌شکل `build(src, target, opts=None, priority=None, channel=None)` است.
> اطلاعات بیشتر: <https://koji.fedoraproject.org/koji/api>.

- فراخوانی تابع ساخت با گزینهٔ scratch:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"scratch": True\}\}'`

- فراخوانی تابع ساخت با گزینهٔ arch_override:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"opts":{"arch_override":"sw_64"\}\}'`

- فراخوانی تابع ساخت در کانال `default`:

`koji call build '"{{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}"' \"{{target}}\" --kwargs '{"channel":"default"}'`

- نمایش راهنما:

`koji call {{[-h|--help]}}`
