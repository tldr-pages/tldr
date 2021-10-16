# scp

> Secure-Copy
> More information: <https://manned.org/scp>.

- Copy File over ssh to remote server

`scp /home/local/file :{{remoteUser}}@:{{remoteHost}}:/var/remote/location`

- Copy File from remote server to local machine

`scp :{{remoteUser}}@:{{remoteHost}}:/var/remote/file /home/local/location`

- Use custom Port

`scp -P :{{remotePort}} :{{command}}`

- Recursion

`scp -r :{{command}}`

- Debug

`scp -v :{{command}}`

- Time and Connection Speed

`scp -p :{{command}}`

- Speedup the transfer using compression

`scp -C :{{command}}`
