# scoop bucket

> 버킷 관리: Git 저장소는 scoop이 애플리케이션을 설치하는 방법을 설명하는 파일을 포함합니다.
> Scoop이 버킷이 위치한 곳을 모르면 저장소 위치를 지정해야 합니다.
> 더 많은 정보: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- 현재 사용 중인 모든 버킷 표시:

`scoop bucket list`

- 알려진 모든 버킷 표시:

`scoop bucket known`

- 알려진 버킷을 이름으로 추가:

`scoop bucket add {{이름}}`

- 이름과 Git 저장소 URL로 알려지지 않은 버킷을 추가:

`scoop bucket add {{이름}} {{https://example.com/repository.git}}`

- 이름으로 버킷 제거:

`scoop bucket rm {{이름}}`
