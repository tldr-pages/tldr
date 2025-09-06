# var-dump-server

> Symfony 덤프 서버.
> Symfony VarDumper 컴포넌트에 의해 덤프된 데이터를 수집합니다.
> 더 많은 정보: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>.

- 서버 시작:

`var-dump-server`

- 데이터를 HTML 파일로 덤프:

`var-dump-server --format=html > {{경로/대상/파일.html}}`

- 특정 주소와 포트에서 서버 수신 대기:

`var-dump-server --host {{127.0.0.1:9912}}`
