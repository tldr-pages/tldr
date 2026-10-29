# wlmail

> Manage emails with Windows Live Mail.
> Some subcommands are not supported in older Windows Mail (`winmail`) for Windows Vista.
> Note: This program is deprecated since Windows 8 in favor of their successors (Mail, New Outlook).
> More information: <https://archive.org/details/windows_live_essentials_2012_qfe4_image>.

- Open Windows Live Mail in the recently-viewed page:

`wlmail`

- Open Windows Live Mail directly into the mail inbox (not supported in `winmail`):

`wlmail /mail`

- Open a `.eml` mail message file in Windows Live Mail:

`wlmail {{/eml|/maileml}}:{{path\to\file.eml}}`

- Open a `mailto:` URI to compose a new message in Windows Live Mail:

`wlmail /mailurl:{{mailto:user@example.com}}`
