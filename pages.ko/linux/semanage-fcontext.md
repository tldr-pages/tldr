# semanage fcontext

> 파일/폴더에 대한 지속적인 SELinux 보안 컨텍스트 규칙 관리.
> 같이 보기: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
> 더 많은 정보: <https://manned.org/semanage-fcontext>.

- 모든 파일 레이블링 규칙 나열:

`sudo semanage fcontext {{[-l|--list]}}`

- 사용자 정의 파일 레이블링 규칙을 헤더 없이 나열:

`sudo semanage fcontext {{[-lCn|--list --locallist --noheading]}}`

- PCRE 정규표현식과 일치하는 경로에 레이블을 지정하는 사용자 정의 규칙 추가:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '{{/mnt/share(/.*)?}}'`

- PCRE 정규표현식을 사용하여 사용자 정의 규칙 삭제:

`sudo semanage fcontext {{[-d|--delete]}} '{{/mnt/share(/.*)?}}'`

- 새로운 규칙을 적용하여 폴더를 재귀적으로 다시 레이블링:

`restorecon -Rv {{경로/대상/폴더}}`
