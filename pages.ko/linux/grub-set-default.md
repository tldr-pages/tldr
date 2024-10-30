# grub-set-default

> GRUB의 기본 부트 항목 설정.
> 더 많은 정보: <https://manned.org/grub-set-default>.

- 기본 부트 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-set-default {{항목_번호}}`

- 대체 부트 디렉토리에 대해 기본 부트 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-set-default --boot-directory {{/경로/대상/부트_디렉토리}} {{항목_번호}}`
