# cat

> Nối và hiển thị nội dung các tệp.
> Thông tin thêm: <https://manned.org/cat.1posix>.

- In nội dung tệp ra `stdout`:

`cat {{đường_dẫn/đến/tệp}}`

- Nối nhiều tệp vào tệp đích:

`cat {{đường_dẫn/đến/tệp1 đường_dẫn/đến/tệp2 ...}} >{{đường_dẫn/đến/tệp_đầu_ra}}`

- Nối thêm nhiều tệp vào cuối tệp đích:

`cat {{đường_dẫn/đến/tệp1 đường_dẫn/đến/tệp2 ...}} >>{{đường_dẫn/đến/tệp_đầu_ra}}`

- Sao chép nội dung tệp vào tệp đích không qua bộ đệm:

`cat -u {{/dev/tty12}} >{{/dev/tty13}}`

- Ghi `stdin` vào một tệp:

`cat - >{{đường_dẫn/đến/tệp}}`
