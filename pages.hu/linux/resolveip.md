# resolveip

> A hosztnevek feloldása IP-címekre és fordítva. További információ: <https://mariadb.com/kb/en/resolveip/>.

- Egy hostnév feloldása IP-címre:

`resolveip {{example.org}}`

- Egy IP-cím feloldása egy hostnévre:

`resolveip {{1.1.1.1}}`

- Csendes üzemmód. Kevesebb kimenetet produkál:

`resolveip --silent {{example.org}}`
