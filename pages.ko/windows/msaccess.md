# msaccess

> Microsoft Office의 데이터베이스 관리 애플리케이션.
> 더 많은 정보: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=access>.

- 데이터베이스 애플리케이션 실행:

`msaccess`

- 기존 데이터베이스 파일 열기:

`msaccess {{경로\대상\파일.accdb}}`

- 기존 데이터베이스 파일을 읽기 전용([r]ead-[o]nly) 모드로 열기:

`msaccess /ro {{경로\대상\파일.accdb}}`

- 데이터베이스를 연 후 지정한 매크로 실행(e[x]ecute):

`msaccess {{경로\대상\파일.accdb}} /x {{매크로_이름}}`
