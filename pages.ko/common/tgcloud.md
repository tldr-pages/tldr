# tgcloud

> Telegram 계정 관리.
> 관련 항목: `tgsend`, `tginfo`, `tgutil`.
> 더 많은 정보: <https://pypi.org/project/telegram-cloud/>.

- 캡션과 함께 파일을 채팅에 업로드:

`tgcloud {{[-m|--mode]}} upload {{[-n|--name]}} {{세션_이름}} {{[-u|--username]}} {{채팅_아이디}} {{[-p|--path]}} {{파일_경로}} {{[-c|--caption]}} {{캡션}}`

- 캡션을 기준으로 채팅에서 파일을 다운로드해 `path/to/store`에 저장:

`tgcloud {{[-m|--mode]}} download {{[-n|--name]}} {{세션_이름}} {{[-u|--username]}} {{채팅_아이디}} {{[-p|--path]}} {{경로/대상/저장소}} {{[-c|--caption]}} {{캡션}}`
