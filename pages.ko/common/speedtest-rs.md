# speedtest-rs

> 비공식 Rust 기반 speedtest.net 네트워크 속도 테스트 도구, HTTP Legacy Fallback 방식만 지원.
> 더 많은 정보: <https://github.com/nelsonjchen/speedtest-rs>.

- 전체 속도 테스트 실행 (다운로드 및 업로드):

`speedtest-rs`

- 거리를 기준으로 정렬된 `speedtest.net` 서버 목록 표시:

`speedtest-rs --list`

- 다운로드 속도만 테스트:

`speedtest-rs --no-upload`

- 업로드 속도만 테스트:

`speedtest-rs --no-download`

- 테스트 결과 이미지의 공유 링크 생성:

`speedtest-rs --share`

- 기본 정보만 간단히 출력:

`speedtest-rs --simple`
