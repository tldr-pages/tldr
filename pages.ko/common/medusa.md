# medusa

> 다양한 프로토콜에 대한 모듈식 병렬 로그인 브루트포싱 도구.
> 더 많은 정보: <https://manned.org/medusa>.

- 설치된 모든 모듈 나열:

`medusa -d`

- 특정 모듈의 사용 예시 보기 (`medusa -d`로 모든 설치된 모듈 나열 가능):

`medusa -M {{ssh|http|web-form|postgres|ftp|mysql|...}} -q`

- 사용자 이름 파일과 비밀번호 파일을 사용하여 FTP 서버에 대해 브루트포싱 실행:

`medusa -M ftp -h host -U {{경로/대상/사용자_이름_파일}} -P {{경로/대상/비밀번호_파일}}`

- 지정된 사용자 이름, 비밀번호, 사용자 에이전트를 사용하여 HTTP 서버에 로그인 시도:

`medusa -M HTTP -h host -u {{사용자_이름}} -p {{비밀번호}} -m USER-AGENT:"{{에이전트}}"`

- 사용자 이름 파일과 해시를 사용하여 MySQL 서버에 대해 브루트포싱 실행:

`medusa -M mysql -h host -U {{경로/대상/사용자_이름_파일}} -p {{해시}} -m PASS:HASH`

- 사용자 이름과 pwdump 파일을 사용하여 SMB 서버 목록에 대해 브루트포싱 실행:

`medusa -M smbnt -H {{경로/대상/호스트_파일}} -C {{경로/대상/pwdump_파일}} -u {{사용자_이름}} -m PASS:HASH`
