# docker container commit

> একটি কন্টেইনারের পরিবর্তন থেকে নতুন ইমেজ তৈরি করুন।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/commit/>।

- নির্দিষ্ট একটি কন্টেইনার থেকে একটি ইমেজ তৈরি করুন:

`docker {{[commit|container commit]}} {{container}} {{image}}:{{tag}}`

- তৈরি করা ইমেজে একটি `CMD` Dockerfile নির্দেশনা প্রয়োগ করুন:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{command}}" {{container}} {{image}}:{{tag}}`

- তৈরি করা ইমেজে একটি `ENV` Dockerfile নির্দেশনা প্রয়োগ করুন:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- মেটাডাটায় নির্দিষ্ট লেখক (author) সহ একটি ইমেজ তৈরি করুন:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{author}}" {{container}} {{image}}:{{tag}}`

- মেটাডাটায় নির্দিষ্ট মন্তব্য (comment) সহ একটি ইমেজ তৈরি করুন:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{comment}}" {{container}} {{image}}:{{tag}}`

- কমিট করার সময় কন্টেইনার pause না করে একটি ইমেজ তৈরি করুন:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{container}} {{image}}:{{tag}}`

- সাহায্য প্রদর্শন করুন:

`docker {{[commit|container commit]}} --help`
