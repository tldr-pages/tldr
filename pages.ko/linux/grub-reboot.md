# grub-reboot

> 다음 부팅에만 적용되는 GRUB의 기본 부팅 항목 설정.
> 더 많은 정보: <https://manned.org/grub-reboot>.

- 다음 부팅을 위해 기본 부팅 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-reboot {{항목_번호}}`

- 다음 부팅을 위해 대체 부팅 디렉토리의 항목 번호, 이름 또는 식별자로 기본 부팅 항목 설정:

`sudo grub-reboot --boot-directory {{/경로/대상/부팅_디렉토리}} {{항목_번호}}`
