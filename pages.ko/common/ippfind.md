# ippfind

> DNS 서버에 등록되었거나 로컬 장치에서 사용할 수 있는 서비스를 검색하는 도구.
> 관련 항목: `ipptool`, `ippeveprinter`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-ippfind.html>.

- 네트워크에 등록된 IPP 프린터와 상태 목록 출력:

`ippfind {{[-l|--ls]}}`

- 네트워크의 모든 PostScript 프린터에 특정 문서 전송:

`ippfind --txt-pdl application/postscript {{[-x|--exec]}} ipptool -f {{경로/대상/문서.ps}} '{}' print-job.test \;`

- 네트워크의 모든 PostScript 프린터에 테스트 문서 전송:

`ippfind --txt-pdl application/postscript {{[-x|--exec]}} ipptool -f onepage-letter.ps '{}' print-job.test \;`

- 이름이 특정 `regex`와 일치하는 PostScript 프린터에 테스트 문서 전송:

`ippfind --txt-pdl application/postscript {{[-h|--host]}} {{regex}} {{[-x|--exec]}} ipptool -f onepage-letter.ps '{}' print-job.test \;`
