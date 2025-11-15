# rankmirrors

> Pacman 미러 목록을 연결 및 열기 속도에 따라 순위 매기기.
> 새로운 미러리스트를 `stdout`에 작성합니다.
> 더 많은 정보: <https://manned.org/rankmirrors>.

- 미러 목록 순위 매기기:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- 상위 순위 서버의 지정된 개수만 출력:

`rankmirrors -n {{개수}} {{/etc/pacman.d/mirrorlist}}`

- 미러리스트 생성 시 자세히 출력:

`rankmirrors -v {{/etc/pacman.d/mirrorlist}}`

- 특정 URL만 테스트:

`rankmirrors --url {{URL}}`

- 전체 미러리스트 대신 응답 시간만 출력:

`rankmirrors --times {{/etc/pacman.d/mirrorlist}}`
