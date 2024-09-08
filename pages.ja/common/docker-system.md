# docker system

> Dockerのデータ管理とシステム全体に関わる情報の表示をします。
> 詳しくはこちら: <https://docs.docker.com/engine/reference/commandline/system/>

- ヘルプの表示をする:

`docker system`

- Dockerディスクの使用量を表示する:

`docker system df`

- ディスクの使用量に関して詳細な情報を表示する:

`docker system df --verbose`

- 不使用データを削除する:

`docker system prune`

- 不使用データのうち指定時間より前に作成されたものを削除する:

`docker system prune --filter "until={{時}}h{{分}}m"`

- Dockerデーモンからのリアルタイムイベントを表示する:

`docker system events`

- コンテナからのリアルタイムイベントを適正なJSON行としてストリーム表示する:

`docker system events --filter 'type=container' --format '{{json .}}'`

- システム全体に関わる情報の表示をする:

`docker system info`
