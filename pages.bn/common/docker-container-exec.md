# docker container exec

> ইতিমধ্যে চলমান একটি Docker কন্টেইনারে কমান্ড চালান।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/exec/>।

- ইতিমধ্যে চলমান একটি কন্টেইনারে একটি ইন্টারঅ্যাক্টিভ শেল সেশনে প্রবেশ করুন:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{/bin/bash}}`

- চলমান কন্টেইনারে ব্যাকগ্রাউন্ডে (detached) একটি কমান্ড চালান:

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- একটি কমান্ড চালানোর জন্য নির্দিষ্ট working directory নির্বাচন করুন:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{path/to/directory}} {{container_name}} {{command}}`

- চলমান কন্টেইনারে ব্যাকগ্রাউন্ডে একটি কমান্ড চালান, কিন্তু `stdin` খোলা রাখুন:

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- চলমান Bash সেশনে একটি environment variable সেট করুন:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- নির্দিষ্ট ব্যবহারকারী হিসেবে একটি কমান্ড চালান:

`docker {{[exec|container exec]}} {{[-u|--user]}} {{user}} {{container_name}} {{command}}`
