# docker container logs

> কন্টেইনার লগ প্রিন্ট করুন।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/logs/>।

- একটি কন্টেইনারের লগ প্রিন্ট করুন:

`docker {{[logs|container logs]}} {{container_name}}`

- লগ প্রিন্ট করুন এবং অনুসরণ করুন:

`docker {{[logs|container logs]}} {{container_name}} {{[-f|--follow]}}`

- শেষ 5 লাইন প্রিন্ট করুন:

`docker {{[logs|container logs]}} {{container_name}} {{[-n|--tail]}} 5`

- লগ প্রিন্ট করুন এবং timestamp যুক্ত করুন:

`docker {{[logs|container logs]}} {{container_name}} {{[-t|--timestamps]}}`

- কন্টেইনার চালুর একটি নির্দিষ্ট সময় পর্যন্ত লগ প্রিন্ট করুন (যেমন: 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{container_name}} --until {{time}}`
