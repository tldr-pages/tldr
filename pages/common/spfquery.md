# spfquery

> Query Sender Policy Framework records to validate e-mail senders.
> More information: <https://www.libspf2.org/>.

- Check if an IP address is allowed to send an e-mail from the specified e-mail address:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}}`

- Turn on debugging output:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}} --debug`
