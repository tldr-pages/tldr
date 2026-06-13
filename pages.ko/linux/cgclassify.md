# cgclassify

> 실행 중인 작업을 `cgroups`로 이동합니다.
> 더 많은 정보: <https://manned.org/cgclassify>.

- 특정 PID를 가진 프로세스를 CPU 계층의 student 컨트롤 그룹으로 이동:

`cgclassify -g {{cpu:student}} {{1234}}`

- `/etc/cgrules.conf` 설정 파일에 기반하여 특정 PID를 가진 프로세스를 컨트롤 그룹으로 이동:

`cgclassify {{1234}}`

- 특정 PID를 가진 프로세스를 CPU 계층의 student 컨트롤 그룹으로 이동(서비스 `cgred`의 데몬이 해당 PID 및 자식의 `cgroups`를 변경하지 않음, `/etc/cgrules.conf` 기반):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
