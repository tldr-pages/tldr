# bpftool

> Az eBPF programok és térképek ellenőrzésére és egyszerű manipulálására szolgáló eszköz. Néhány alparancsnak, mint például a `bpftool prog`, saját használati dokumentációja van. További információ: <https://manned.org/bpftool>.

- A betöltött `eBPF` programokról szóló információk listázása:

`bpftool prog list`

- List `eBPF` programcsatolások listája a kernel hálózati alrendszerében:

`bpftool net list`

- Listázza az összes aktív linket:

`bpftool link list`

- Az összes `raw_tracepoint`, `tracepoint`, `kprobe` csatolmányok listája a rendszerben:

`bpftool perf list`

- A `BPF Type Format (BTF)` adatok listázása:

`bpftool btf list`

- A betöltött térképekről szóló információk listázása:

`bpftool map list`

- Az "eth0" hálózati eszköz szondázása a támogatott `eBPF` funkciókért:

`bpftool feature probe dev {{eth0}}`

- Parancsok futtatása kötegelt módban egy fájlból:

`bpftool batch file {{myfile}}`
