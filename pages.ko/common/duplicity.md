# duplicity

> 증분, 압축, 암호화 및 버전별 백업을 생성.
> 다양한 백엔드 서비스에 백업을 업로드할 수도 있음.
> 버전에 따라 일부 옵션을 사용하지 못할 수도 있음 (예: 2.0.0의 `--gio`).
> 더 많은 정보: <https://duplicity.gitlab.io/stable/duplicity.1.html#name>.

- FTPS를 통해 디렉터리를 원격 시스템에 백업하고, 비밀번호로 암호화:

`FTP_PASSWORD={{ftp_로그인_비밀번호}} PASSPHRASE={{암호_비밀번호}} duplicity {{경로/대상/소스/디렉토리}} {{ftps://사용자@호스트명/타겟/디렉토리/경로/}}`

- 매월 전체 백업을 수행하여 Amazon S3에 디렉터리를 백업:

`duplicity --full-if-older-than {{1M}} s3://{{버킷_이름[/접두사]}}`

- WebDAV 공유에 저장된 백업에서 1년이 넘은 버전을 삭제:

`FTP_PASSWORD={{webdav_로그인_비밀번호}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://사용자@호스트명[:포트]/일부_디렉토리}}`

- 사용 가능한 백업을 나열:

`duplicity collection-status "file://{{절대/경로/대상/백업/디렉토리}}"`

- SSH를 통해 원격 시스템에 저장된 백업의 파일을 나열:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{사용자@호스트명}}/{{경로/대상/백업/디렉토리}}`

- GnuPG로 암호화된 로컬 백업의 하위 디렉토리를 지정된 위치로 복원:

`PASSPHRASE={{gpg_키_비밀번호}} duplicity restore --encrypt-key {{gpg_키_아이디}} --path-to-restore {{상대/경로/복원된디렉토리}} file://{{절대/경로/대상/백업/디렉토리}} {{경로/대상/디렉토리/대상/복원/대상}}`
