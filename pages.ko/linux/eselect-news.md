# eselect news

> Gentoo 뉴스 항목을 읽기 위한 `eselect` 모듈.
> 참고: 저장소가 동기화되고 읽지 않은 뉴스 항목이 있을 때 Portage가 알림을 출력합니다.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#News>.

- 사용 가능한 뉴스 항목과 번호 나열 (기본적으로 모두):

`eselect news list {{all|new}}`

- 지정된 뉴스 항목 출력:

`eselect news read {{번호1 번호2 ...}}`

- 읽지 않은 모든 뉴스 항목 출력:

`eselect news read`

- 지정된 뉴스 항목을 읽지 않음으로 표시:

`eselect news unread {{번호1 번호2 ...}}`

- 읽은 모든 뉴스 항목 삭제:

`eselect news purge`

- 사용 가능한 뉴스 항목 수 출력 (기본적으로 새 항목):

`eselect news count {{all|new}}`
