# carthage

> Cocoa 애플리케이션을 위한 의존성 관리 도구.
> 더 많은 정보: <https://github.com/Carthage/Carthage>.

- Cartfile에 언급된 모든 의존성을 최신 버전으로 다운로드하고 빌드:

`carthage update`

- 의존성을 업데이트하되, iOS용으로만 빌드:

`carthage update --platform ios`

- 의존성을 업데이트하되, 빌드하지 않음:

`carthage update --no-build`

- 현재 버전의 의존성을 다운로드하고 재빌드(업데이트하지 않음):

`carthage bootstrap`

- 특정 의존성을 재빌드:

`carthage build {{의존성}}`
