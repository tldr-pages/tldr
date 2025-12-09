# secon

> 파일, 프로세스 ID, 현재 실행 컨텍스트 또는 컨텍스트 명세의 SELinux 보안 컨텍스트를 확인합니다.
> 같이 보기: `semanage`, `runcon`, `chcon`.
> 더 많은 정보: <https://manned.org/secon>.

- 현재 실행 컨텍스트의 보안 컨텍스트 확인:

`secon`

- 프로세스의 현재 보안 컨텍스트 확인:

`secon --pid {{1}}`

- 모든 중간 심볼릭 링크를 해석하여 파일의 현재 보안 컨텍스트 확인:

`secon --file {{경로/대상/파일_또는_폴더}}`

- 심볼릭 링크 자체의 현재 보안 컨텍스트 확인 (즉, 해석하지 않음):

`secon --link {{경로/대상/심볼릭_링크}}`

- 컨텍스트 명세를 해석하고 설명:

`secon {{system_u:system_r:container_t:s0:c899,c900}}`
