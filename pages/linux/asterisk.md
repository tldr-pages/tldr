# asterisk

> Run and manage telephone and exchange (phone) server instances.
> More information: <https://wiki.asterisk.org/wiki/display/AST/Home>.

- [R]econnect to a running server, and turn on logging 3 levels of [v]erbosity:

`asterisk -r -vvv`

- [R]econnect to a running server, run a single command, and return:

`asterisk -r -x "{{command}}"`

- Show chan_SIP clients (phones):

`asterisk -r -x "sip show peers"`

- Show active calls and channels:

`asterisk -r -x "core show channels"`

- Show voicemail mailboxes:

`asterisk -r -x "voicemail show users"`

- Terminate a channel:

`asterisk -r -x "hangup request {{channel_ID}}"`

- Reload chan_SIP configuration:

`asterisk -r -x "sip reload"`
