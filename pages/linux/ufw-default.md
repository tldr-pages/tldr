# ufw-default

> Change the default policy for traffic based on direction.
> More information: <https://manned.org/ufw>.

- Allow traffic going a certain direction:

`sudo ufw default allow {{incoming|outgoing|routed}}`

- Deny traffic going a certain direction:

`sudo ufw default deny {{incoming|outgoing|routed}}`

- Reject traffic going a certain direction:

`sudo ufw default reject {{incoming|outgoing|routed}}`
