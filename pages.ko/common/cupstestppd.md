# cupstestppd

> 사양 버전 4.3에 대한 PPD 파일의 적합성 테스트.
> 오류 코드 (각각 1, 2, 3, 4): 잘못된 CLI 인수, 파일을 열 수 없음, 건너뛸 수 없는 형식 오류 및 PPD 사양 불일치.
> 참고: 이 명령은 더 이상 사용되지 않음.
> 더 보기: `lpadmin`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-cupstestppd.html>.

- 자동 모드에서 하나 이상의 파일의 적합성을 테스트:

`cupstestppd -q {{경로/대상/파일1.ppd 경로/대상/파일2.ppd ...}}`

- 자세한 적합성 테스트 결과를 보여주는 `stdin`에서 PPD 파일을 가져옴:

`cupstestppd -v - < {{경로/대상/파일.ppd}}`

- 현재 디렉터리 아래의 모든 PPD 파일을 테스트하고, 일치하지 않는 각 파일의 이름을 인쇄:

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`
