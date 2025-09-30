# sport

> SlackBuilds 검색 및 설치.
> 더 많은 정보: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- `sport`를 처음 실행하기 위해 SlackBuild 목록 가져오기:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- `rsync`를 통해 시스템 트리의 업데이트 가져오기:

`sudo sport rsync`

- 이름으로 패키지 검색:

`sport search "{{키워드}}"`

- 패키지가 설치되었는지 확인:

`sport check {{패키지}}`

- 패키지의 README 및 `.info` 파일 표시:

`sport cat {{패키지}}`

- 의존성이 해결된 후 패키지 설치:

`sudo sport install {{패키지}}`

- 파일에 있는 패키지 목록 설치 (형식: 공백으로 구분된 패키지):

`sudo sport install $(< {{경로/대상/목록}})`
