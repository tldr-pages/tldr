# npm hook

> 패키지를 위한 `npm` 레지스트리 훅을 관리하는 명령어.
> 참고: 이 명령어는 현재 deprecated 상태입니다.
> 더 많은 정보: <https://docs.npmjs.com/cli/v10/hook/>.

- 활성화된 모든 훅 목록 출력:

`npm hook ls`

- 특정 패키지에 새로운 훅 추가:

`npm hook add {{패키지_이름}} {{이벤트}} {{타겟_주소}}`

- ID로 특정 훅 제거:

`npm hook rm {{훅_아이디}}`

- 새로운 정보로 훅 업데이트:

`npm hook update {{훅_아이디}} {{타겟_주소}}`
