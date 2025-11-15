# gallery-dl

> 여러 이미지 호스팅 사이트에서 이미지 갤러리와 컬렉션 다운로드.
> 더 많은 정보: <https://github.com/mikf/gallery-dl>.

- 지정된 URL에서 이미지 다운로드:

`gallery-dl "{{url}}"`

- 웹 브라우저에서 기존 쿠키를 검색 (로그인이 필요한 사이트에 유용):

`gallery-dl --cookies-from-browser {{browser}} "{{주소}}"`

- 사용자 이름과 비밀번호를 사용하여 인증을 지원하는 사이트에서 이미지의 직접 URL을 가져옴:

`gallery-dl --get-urls --username {{사용자명}} --password {{비밀번호}} "{{주소}}"`

- 장 번호와 언어별로 만화 장을 필터링:

`gallery-dl --chapter-filter "{{10 <= chapter < 20}}" --option "lang={{언어_코드}}" "{{주소}}"`
