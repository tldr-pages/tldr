# emaint

> Portage 유지 관리 작업을 수행.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Portage#emaint>.

- 자동 동기화가 설정된 저장소 동기화 (대부분의 저장소에서 기본값):

`sudo emaint sync {{[-a|--auto]}}`

- 지정한 저장소 동기화:

`sudo emaint sync {{[-r|--repo]}} {{저장소}}`

- 모든 저장소 동기화:

`sudo emaint sync {{[-A|--allrepos]}}`

- Portage 재개 목록 정리:

`sudo emaint cleanresume {{[-f|--fix]}}`

- Portage 로그 정리:

`sudo emaint logs {{[-C|--clean]}}`
