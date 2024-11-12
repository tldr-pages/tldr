# certutil

> NSS 데이터베이스와 기타 NSS 토큰 모두에서 키와 인증서를 관리.
> 더 많은 정보: <https://manned.org/certutil>.

- 현재 디렉터리([d]irectory)에 새로운([N]ew) 인증서 데이터베이스를 만듬:

`certutil -N -d .`

- 데이터베이스의 모든 인증서를 나열:

`certutil -L -d .`

- 비밀번호 파일([f]ile)을 지정하는 데이터베이스의 모든 개인 키([K]eys)를 나열:

`certutil -K -d . -f {{경로/대상/패스워드_파일.txt}}`

- 닉네임([n]ickname), 신뢰 속성([t]rust attributes) 및 입력([i]nput) CRT 파일을 지정하여 요청자 데이터베이스에 서명된 인증서를 추가([A]dd):

`certutil -A -n "{{서버_인증서}}" -t ",," -i {{경로/대상/파일.crt}} -d .`

- Add subject alternative names to a given [c]ertificate with a specific key size ([g]):

`certutil -S -f {{경로/대상/패스워드_파일.txt}} -d . -t ",," -c "{{서버_인증서}}" -n "{{서버_이름}}" -g {{2048}} -s "CN={{공통_이름}},O={{조직}}"`
