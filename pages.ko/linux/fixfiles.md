# fixfiles

> 파일의 SELinux 보안 컨텍스트를 수정합니다.
> 더 많은 정보: <https://manned.org/fixfiles>.

- onboot와 함께 지정되면, 이 fixfiles는 `/.autorelabel` 파일에 현재 날짜를 기록하여 나중에 레이블링 속도를 높이는 데 사용할 수 있습니다. restore와 함께 사용하면 오늘 수정된 파일에만 영향을 줍니다:

`fixfiles -B`

- 사용자 지정 가능한 파일에 대해 `file_context`와 일치하도록 컨텍스트를 [F]orce 리셋:

`fixfiles -F`

- 확인 없이 `/tmp` 폴더를 삭제:

`fixfiles -f`

- [R]pm 데이터베이스를 사용하여 특정 패키지 내 모든 파일을 찾아 파일 컨텍스트 복원:

`fixfiles -R {{rpm_패키지1,rpm_패키지2 ...}}`

- `PREVIOUS_FILECONTEXT` 파일과 현재 설치된 파일의 차이를 비교하고, 영향을 받은 모든 파일의 컨텍스트를 복원:

`fixfiles -C PREVIOUS_FILECONTEXT`

- find `--newermt` 명령어에 전달될 특정 날짜 이후에 생성된 파일에만 작동:

`fixfiles -N {{YYYY-MM-DD HH:MM}}`

- 다시 레이블링하기 전에 파일 시스템을 [M]ount 바인딩하여, 마운트된 파일 또는 폴더의 컨텍스트를 수정할 수 있도록 설정:

`fixfiles -M`

- 진행 상태에서 자세히로 [v]자세히 설정을 변경하고 `-p` 대신 `-v`로 `restorecon` 실행:

`fixfiles -v`
