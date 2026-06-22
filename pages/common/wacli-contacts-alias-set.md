# wacli contacts alias set

> Set a custom alias for a WhatsApp contact.
> See also: `wacli contacts show`, `wacli contacts search`.
> More information: <https://github.com/steipete/wacli>.

- Set an alias for a specific contact:

`wacli contacts alias set {{phone_number}}@s.whatsapp.net {{alias}}`

- Set an alias using a custom store:

`wacli contacts alias set {{phone_number}}@s.whatsapp.net {{alias}} --store {{path/to/store}}`
