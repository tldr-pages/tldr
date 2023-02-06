# ifup

> A hálózati interfészek engedélyezéséhez használt eszköz. További információ: <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Engedélyezze az eth0 interfészt:

`ifup {{eth0}}`

- Engedélyezi az összes "auto"-val definiált interfészt a `/etc/network/interfaces` oldalon:

`ifup -a`
