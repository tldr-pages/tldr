# netstat

> 開いている接続、開いているソケットポートなどのネットワーク関連情報を表示します。
> 参照: `ss`。
> もっと詳しく: <https://manned.org/netstat>。

- 全てのポートを一覧表示する:

`netstat {{[-a|--all]}}`

- 全てのリスニングポートを一覧表示する:

`netstat {{[-l|--listening]}}`

- リッスン中のTCPポートを一覧表示する:

`netstat {{[-t|--tcp]}}`

- PIDとプログラム名を表示する:

`netstat {{[-p|--program]}}`

- 情報を連続的に一覧表示する:

`netstat {{[-c|--continuous]}}`

- ルートを一覧表示し、IPアドレスをホスト名に解決しない:

`netstat {{[-rn|--route --numeric]}}`

- リッスンしているTCPポートとUDPポートを一覧表示する (+ rootの場合はユーザーとプロセス):

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`
