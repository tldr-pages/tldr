# ufw default

> Set the default policy for the Uncomplicated Firewall.
> See also: `ufw`, `ufw status`, `ufw allow`.
> More information: <https://manned.org/ufw>.

- Set the default policy for incoming traffic:

`sudo ufw default {{allow|deny|reject}} incoming`

- Set the default policy for outgoing traffic:

`sudo ufw default {{allow|deny|reject}} outgoing`

- Set the default policy for routed traffic:

`sudo ufw default {{allow|deny|reject}} routed`
