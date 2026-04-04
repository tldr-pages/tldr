# docker container ls

> Docker কন্টেইনার তালিকাভুক্ত করুন।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/ls/>।

- বর্তমানে চলমান Docker কন্টেইনারগুলো তালিকাভুক্ত করুন:

`docker {{[ps|container ls]}}`

- সব Docker কন্টেইনার তালিকাভুক্ত করুন (চলমান এবং বন্ধ):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- সর্বশেষ তৈরি করা কন্টেইনার দেখান (সকল অবস্থাসহ):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- নামের মধ্যে নির্দিষ্ট substring থাকা কন্টেইনার ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{name}}"`

- নির্দিষ্ট ইমেজকে ancestor হিসেবে শেয়ার করে এমন কন্টেইনার ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- exit status code অনুযায়ী কন্টেইনার ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- status অনুযায়ী কন্টেইনার ফিল্টার করুন (created, running, removing, paused, exited, এবং dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- নির্দিষ্ট একটি volume mount করে, অথবা নির্দিষ্ট path-এ volume mount করা কন্টেইনার ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
