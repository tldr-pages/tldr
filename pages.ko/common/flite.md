# flite

> 음성 합성 엔진.
> 더 많은 정보: <http://www.festvox.org/flite/doc/>.

- 사용 가능한 모든 음성을 나열:

`flite -lv`

- 텍스트 문자열을 음성으로 변환:

`flite -t "{{문자열}}"`

- 파일 내용을 음성으로 변환:

`flite -f {{경로/대상/파일.txt}}`

- 지정된 음성 사용:

`flite -voice {{file://경로/대상/파일이름.flitevox|url}}`

- 출력을 wav 파일에 저장:

`flite -voice {{file://경로/대상/파일이름.flitevox|url}} -f {{경로/대상/파일.txt}} -o {{츨력파일.wav}}`

- 버전 정보 표시:

`flite --version`
