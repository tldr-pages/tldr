# netstat

> 開いている接続、開いているソケットポートなどのネットワーク関連情報を表示します。
> `ss` も参照してください。
> もっと詳しく: <https://manned.org/netstat>。

- 全てのポートを一覧表示する:

`netstat --all`

- 全てのリスニングポートを一覧表示する:

`netstat --listening`

- リッスン中のTCPポートを一覧表示する:

`netstat --tcp`

- PIDとプログラム名を表示する:

`netstat --program`

- 情報を連続的に一覧表示する:

`netstat --continuous`

- ルートを一覧表示し、IPアドレスをホスト名に解決しない:

`netstat --route --numeric`

- リッスンしているTCPポートとUDPポートを一覧表示する (+ rootの場合はユーザーとプロセス):

`netstat --listening --program --numeric --tcp --udp --extend`
