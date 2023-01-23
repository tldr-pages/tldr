# chcpu

> A rendszer processzorainak engedélyezése/letiltása. További információ: <https://manned.org/chcpu>.

- A CPU-k letiltása a CPU-azonosítószámok listáján keresztül:

`chcpu -d {{1,3}}`

- A CPU-k egy csoportjának engedélyezése a CPU-azonosítószámok tartományán keresztül:

`chcpu -e {{1-10}}`
