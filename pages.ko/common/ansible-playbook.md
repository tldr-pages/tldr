# ansible-playbook

> SSH를 통해 원격 머신에서 playbook에 정의된 작업 실행. 
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- playbook에서 작업 실행:

`ansible-playbook {{playbook}}`

- 사용자 정의 호스트 인벤토리를 포함한 playbook에서 작업 실행:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- 명령어 라인을 통해 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- json 파일에 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`