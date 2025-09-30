# duti

> macOS에서 문서 유형 및 URL 스킴에 대한 기본 애플리케이션 설정.
> 더 많은 정보: <https://github.com/moretension/duti>.

- HTML 문서의 기본 처리기로 Safari 설정:

`duti -s {{com.apple.Safari}} {{public.html}} all`

- `.m4v` 확장자를 가진 파일의 기본 뷰어로 VLC 설정:

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- ftp:// URL 스킴의 기본 처리기로 Finder 설정:

`duti -s {{com.apple.Finder}} "{{ftp}}"`

- 주어진 확장자의 기본 애플리케이션 정보 표시:

`duti -x {{확장자}}`

- 주어진 UTI의 기본 처리기 표시:

`duti -d {{uti}}`

- 주어진 UTI의 모든 처리기 표시:

`duti -l {{uti}}`
