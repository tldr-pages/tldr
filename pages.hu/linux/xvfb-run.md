# xvfb-run

> Parancs futtatása virtuális X-kiszolgáló környezetben. További információ: <https://www.x.org/wiki/>.

- A megadott parancs futtatása virtuális X-kiszolgálóban:

`xvfb-run {{command}}`

- Próbáljon meg egy szabad kiszolgálószámot kapni, ha az alapértelmezett (99) nem elérhető:

`xvfb-run --auto-servernum {{command}}`

- Adjon át argumentumokat az Xvfb kiszolgálónak:

`xvfb-run --server-args "{{-screen 0 1024x768x24}}" {{command}}`
