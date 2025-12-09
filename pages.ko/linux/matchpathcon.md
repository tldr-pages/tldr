# matchpathcon

> 경로의 지속적인 SELinux 보안 컨텍스트 설정을 조회합니다.
> 같이 보기: `semanage-fcontext`, `secon`, `chcon`, `restorecon`.
> 더 많은 정보: <https://manned.org/matchpathcon.8>.

- 절대 경로의 지속적인 보안 컨텍스트 설정 조회:

`matchpathcon {{/경로/대상/파일}}`

- 특정 파일 유형에 대한 설정으로 조회 제한:

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} {{/경로/대상/파일}}`

- 경로의 지속적인 보안 컨텍스트와 현재 보안 컨텍스트가 일치하는지 [v]확인:

`matchpathcon -V {{/경로/대상/파일}}`
