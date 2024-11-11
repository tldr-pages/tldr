# warp-diag

> Cloudflare의 WARP 서비스 진단 및 피드백 도구.
> 같이 보기: `warp-cli`.
> 더 많은 정보: <https://developers.cloudflare.com/warp-client/>.

- 시스템 구성 및 WARP 연결 정보가 포함된 Zip 파일 생성:

`warp-diag`

- 디버그 정보를 포함하고 출력 파일명에 타임스탬프를 추가하여 Zip 파일 생성:

`warp-diag --add-ts`

- 특정 폴더에 출력 파일 저장:

`warp-diag --output {{경로/대상/폴더}}`

- Cloudflare의 WARP에 새로운 피드백을 대화형으로 제출:

`warp-diag feedback`
