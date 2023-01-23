# sysctl

> Hozzáférés a kernel állapotára vonatkozó információkhoz. További információ: <https://ss64.com/osx/sysctl.html>.

- Az összes elérhető változó és értékük megjelenítése:

`sysctl -a`

- Apple modell azonosítójának megjelenítése:

`sysctl -n hw.model`

- CPU modell megjelenítése:

`sysctl -n machdep.cpu.brand_string`

- A rendelkezésre álló CPU-funkciók megjelenítése (MMX, SSE, SSE2, SSE3, AES stb.):

`sysctl -n machdep.cpu.features`

- Változtatható kernelállapotváltozó beállítása:

`sysctl -w {{section.tunable}}={{value}}`
