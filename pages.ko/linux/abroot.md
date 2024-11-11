# abroot

> 2개의 루트 파티션 상태(A⟺B) 간 트랜잭션을 통해 완전한 불변성과 원자성을 제공하는 유틸리티.
> 항상 시스템이 일관된 상태를 유지하도록 OCI 이미지를 사용하여 업데이트를 수행합니다.
> 더 많은 정보: <https://github.com/Vanilla-OS/ABRoot>.

- 로컬 이미지에 패키지 추가 (참고: 이 명령을 실행한 후 변경 사항을 적용해야 합니다):

`sudo abroot pkg add {{패키지}}`

- 로컬 이미지에서 패키지 제거 (참고: 이 명령을 실행한 후 변경 사항을 적용해야 합니다):

`sudo abroot pkg remove {{패키지}}`

- 로컬 이미지에 있는 패키지 나열:

`sudo abroot pkg list`

- 로컬 이미지의 변경 사항 적용 (참고: 이러한 변경 사항을 적용하려면 시스템을 재부팅해야 합니다):

`sudo abroot pkg apply`

- 시스템을 이전 상태로 롤백:

`sudo abroot rollback`

- 커널 매개변수 편집/보기:

`sudo abroot kargs {{edit|show}}`

- 상태 표시:

`sudo abroot status`

- 도움말 표시:

`abroot --help`
