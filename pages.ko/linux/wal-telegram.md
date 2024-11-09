# wal-telegram

> pywal/wal이 생성한 색상을 기반으로 Telegram 테마를 생성.
> 더 많은 정보: <https://github.com/guillaumeboehm/wal-telegram>.

- wal의 팔레트와 현재 배경화면(feh 전용)으로 생성:

`wal-telegram`

- wal의 팔레트와 지정된 배경 이미지로 생성:

`wal-telegram --background={{경로/대상/이미지}}`

- wal의 팔레트와 팔레트를 기반으로 한 색상 배경으로 생성:

`wal-telegram --tiled`

- 배경 이미지에 가우시안 블러 적용:

`wal-telegram -g`

- 생성된 테마의 저장 위치 지정(기본값은 `$XDG_CACHE_HOME/wal-telegram` 또는 `~/.cache/wal-telegram`):

`wal-telegram --destination={{경로/대상/저장소}}`

- 생성 후 Telegram 앱 재시작:

`wal-telegram --restart`
