# ippeveprinter

> 간단한 IPP Everywhere 프린터 서버.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>.

- 특정 서비스 이름으로 서버 실행:

`ippeveprinter "{{서비스_이름}}"`

- PPD 파일에서 프린터 속성 로드:

`ippeveprinter -P {{경로/대상/파일.ppd}} "{{서비스_이름}}"`

- 작업이 전송될 때마다 `file` 명령어 실행:

`ippeveprinter -c {{/usr/bin/file}} "{{서비스_이름}}"`

- 출력 파일을 저장할 디렉터리 지정 (기본으로, 사용자 임시 디렉터리 하위에 저아됨):

`ippeveprinter -d {{spool_directory}} "{{서비스_이름}}"`

- 출력 문서를 삭제하지 않고 spool 디렉터리에 유지:

`ippeveprinter -k "{{서비스_이름}}"`

- 프린터 속도(페이지/분) 설정 (기본: 10):

`ippeveprinter -s {{속도}} "{{서비스_이름}}"`
