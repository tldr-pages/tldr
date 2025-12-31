# checksec

> 실행 파일의 보안 속성을 확인.
> 더 많은 정보: <https://manned.org/checksec>.

- 실행 가능한 바이너리 파일의 보안 속성을 확인:

`checksec --file={{경로/대상/바이너리}}`

- 디렉터리에 있는 모든 실행 파일의 보안 속성을 반복적으로 나열:

`checksec --dir={{경로/대상/디렉터리}}`

- 프로세스의 보안 속성을 나열:

`checksec --proc={{pid}}`

- 실행 중인 커널의 보안 속성을 나열:

`checksec --kernel`
