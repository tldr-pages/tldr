# aws ec2

> AWS EC2 인스턴스 및 볼륨 관리.
> AWS EC2는 더 빠른 애플리케이션 개발과 배포를 위해 AWS 클라우드에서 안전하고 크기 조정이 가능한 컴퓨팅 용량을 제공.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- 특정 인스턴스의 정보 출력:

`aws ec2 describe-instances --instance-ids {{인스턴스_아이디}}`

- 모든 인스턴스에 대한 정보 출력:

`aws ec2 describe-instances`

- 모든 EC2 볼륨에 대한 정보 출력:

`aws ec2 describe-volumes`

- EC2 볼륨 삭제:

`aws ec2 delete-volume --volume-id {{볼륨_아이디}}`

- EC2 볼륨에서 스냅샷 생성:

`aws ec2 create-snapshot --volume-id {{볼륨_아이디}}`

- 사용 가능한 AMIs (Amazon 머신 이미지) 목록 나열:

`aws ec2 describe-images`

- 모든 사용 가능한 EC2 명령어 나열:

`aws ec2 help`

- 특정 EC2 하위 명령어 도움말 표시:

`aws ec2 {{subcommand}} help`
