# asterisk

> Telephone and exchange (phone) server.
> Used for running the server itself, and managing an already running instance.
> More information: <https://wiki.asterisk.org/wiki/display/AST/Home/>.

- Connect to a running server, and turn on some logging:

`asterisk -r -vvv`

- Show chan_SIP clients (phones):

`asterisk -r -x "sip show peers"`

- Show active calls & channels:

`asterisk -r -x "core show channels"`

- Show voicemail mailboxes:

`asterisk -r -x "voicemail show users"`

- Terminate a channel:

`asterisk -r -x "hangup request {{channel_ID}}"`

- Reload chan_SIP configuration:

`asterisk -r -x "sip reload"`
