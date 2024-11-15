# setenforce

> SELinux를 강제 모드와 허용 모드 사이에서 전환.
> SELinux를 활성화하거나 비활성화하려면 `/etc/selinux/config`를 편집하세요.
> 같이 보기: `getenforce`, `semanage-permissive`.
> 더 많은 정보: <https://manned.org/setenforce>.

- SELinux를 강제 모드로 설정:

`setenforce {{1|Enforcing}}`

- SELinux를 허용 모드로 설정:

`setenforce {{0|Permissive}}`
