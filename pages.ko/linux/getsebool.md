# getsebool

> SELinux 부울 값 가져오기.
> 같이 보기: `semanage-boolean`, `setsebool`.
> 더 많은 정보: <https://manned.org/getsebool>.

- 특정 부울의 현재 설정 보기:

`getsebool {{httpd_can_connect_ftp}}`

- 모든 부울의 현재 설정 보기:

`getsebool -a`

- 설명과 함께 모든 부울의 현재 설정 보기:

`sudo semanage boolean {{[-l|--list]}}`
