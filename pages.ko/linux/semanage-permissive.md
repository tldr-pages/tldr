# semanage permissive

> 지속적인 SELinux 허용 도메인 관리.
> 이로 인해 프로세스가 비구속 상태가 될 수 있으므로, 장기적으로 사용할 경우 SELinux를 올바르게 구성하는 것이 좋습니다.
> 같이 보기: `semanage`, `getenforce`, `setenforce`.
> 더 많은 정보: <https://manned.org/semanage-permissive>.

- 허용 모드에 있는 모든 프로세스 유형(도메인) 나열:

`sudo semanage permissive {{[-l|--list]}}`

- 도메인에 대한 허용 모드를 설정하거나 해제:

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`
