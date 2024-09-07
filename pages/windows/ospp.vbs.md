# ospp.vbs

> Install, activate, and manage volume licensed versions of Microsoft Office products.
> Note: this command may override, deactivate, and/or remove your current volume of licensed Office product versions, so please proceed cautiously.
> More information: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Install a product key (Note: it replaces the existing key):

`cscript ospp.vbs /inpkey:{{product_key}}`

- Uninstall an installed product key with the last five digits of the product key:

`cscript ospp.vbs /unpkey:{{product_key_digits}}`

- Set a KMS host name:

`cscript ospp.vbs /sethst:{{ip|hostname}}`

- Set a KMS port:

`cscript ospp.vbs /setprt:{{port}}`

- Activate installed Office product keys:

`cscript ospp.vbs /act`

- Display license information for installed product keys:

`cscript ospp.vbs /dstatus`
