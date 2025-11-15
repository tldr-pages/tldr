# onionsearch

> 다양한 `.onion` 검색 엔진에서 URL을 스크랩.
> 참고: `onionsearch`는 `localhost:9050`에서 실행되는 Tor 프록시가 필요하며, `.onion` 웹사이트를 방문하려면 Tor 지원 브라우저가 필요합니다.
> 더 많은 정보: <https://github.com/megadose/OnionSearch>.

- 모든 검색 엔진에서 결과 요청:

`onionsearch "{{문자열}}"`

- 특정 검색 엔진에서 검색 결과 요청:

`onionsearch "{{문자열}}" --engines {{tor66 deeplink phobos ...}}`

- 검색 시 특정 검색 엔진 제외:

`onionsearch "{{문자열}}" --exclude {{candle ahmia ...}}`

- 엔진당 로드할 페이지 수 제한:

`onionsearch "{{stuxnet}}" --engines {{tor66 deeplink phobos ...}} --limit {{3}}`

- 지원되는 모든 검색 엔진 나열:

`onionsearch --help | grep -A1 -i "supported engines"`
