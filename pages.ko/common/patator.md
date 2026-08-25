# patator

> 모듈형 구조 및 유연한 사용 가능한 다목적 brute-force 도구.
> 더 많은 정보: <https://github.com/lanjelot/patator/wiki/Usage>.

- 속도 제한과 타임아웃 옵션을 설정해 SSH 로그인 brute force 수행 (성공 시 로그인 배너 등으로 확인 가능):

`patator ssh_login host={{아이피_또는_호스트}} user=FILE0 password=FILE1 0={{경로/대상/사용자목록.txt}} 1={{경로/대상/비밀번호.txt}} --rate_limit={{초}} --timeout={{초}} -x ignore:mesg='Authentication failed.'`

- 암호화된 ZIP 파일 Brute force 수행:

`patator unzip_pass zipfile={{경로/대상/파일.zip}} password=FILE0 0={{경로/대상/비밀번호.txt}} -x ignore:code!=0`

- HTTP Basic 인증 Brute force (`userpass.txt`는 `username:password` 형식이어야 함):

`patator http_fuzz url={{http://host:port}} auth_type=basic user_pass=COMBO00:COMBO01 0={{경로/대상/사용자_비밀번호_파일.txt}} -x ignore:code=401`

- FTP/FTPS 로그인 Brute force:

`patator ftp_login host={{아이피_또는_호스트}} user=FILE0 password=FILE1 0={{경로/대상/사용자목록.txt}} 1={{경로/대상/비밀번호.txt}} tls={{0|1}} -x ignore:mesg='Login incorrect.' -x ignore,reset,retry:code=500`

- 사용 가능한 모든 모듈 목록 출력:

`patator --help`

- 특정 모듈에 대한 도움말 표시:

`patator {{모듈_이름}} --help`
