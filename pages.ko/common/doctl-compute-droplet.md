# doctl compute droplet

> 드롭릿이라고 불리는 가상 머신을 나열, 생성, 삭제.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- 드롭릿 생성:

`doctl compute droplet create --region {{지역}} --image {{os_이미지}} --size {{vps_타입}} {{드롭릿_이름}}`

- 드롭릿 삭제:

`doctl compute droplet delete {{드롭릿_아이디|드롭릿_이름}}`

- 드롭릿 나열:

`doctl compute droplet list`
