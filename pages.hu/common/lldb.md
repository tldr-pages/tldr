# lldb

> Az LLVM alacsony szintű hibakereső. További információ: <https://lldb.llvm.org>.

- Végrehajtható program hibakeresése:

`lldb {{executable}}`

- A `lldb` csatolása egy adott PID-vel rendelkező futó folyamathoz:

`lldb -p {{pid}}`

- Várjon egy új folyamat indítására egy adott névvel, és csatoljon hozzá:

`lldb -w -n {{process_name}}`
