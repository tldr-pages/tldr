# ipconfig

> Windowsのネットワーク構成を表示および管理します。
> 詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>

- ネットワークアダプタのリストを表示します:

`ipconfig`

- ネットワークアダプタの詳細なリストを表示します:

`ipconfig /all`

- ネットワークアダプタのIPアドレスを更新します:

`ipconfig /renew {{adapter}}`

- ネットワークアダプタのIPアドレスを解放します:

`ipconfig /release {{adapter}}`

- DNSキャッシュからすべてのデータを削除します:

`ipconfig /flushdns`
