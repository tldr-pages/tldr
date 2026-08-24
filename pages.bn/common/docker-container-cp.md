# docker container cp

> হোস্ট এবং কন্টেইনার ফাইলসিস্টেমের মধ্যে ফাইল বা ডিরেক্টরি কপি করুন।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/cp/>।

- হোস্ট থেকে কন্টেইনারে একটি ফাইল বা ডিরেক্টরি কপি করুন:

`docker {{[cp|container cp]}} {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- কন্টেইনার থেকে হোস্টে একটি ফাইল বা ডিরেক্টরি কপি করুন:

`docker {{[cp|container cp]}} {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- হোস্ট থেকে কন্টেইনারে একটি ফাইল বা ডিরেক্টরি কপি করুন এবং symlink অনুসরণ করুন (symlink নিজে কপি না করে symlink করা ফাইলগুলো সরাসরি কপি করে):

`docker {{[cp|container cp]}} {{[-L|--follow-link]}} {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
