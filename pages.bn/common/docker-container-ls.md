# docker container ls

> Docker কন্টেইনারগুলো তালিকাভুক্ত করুন।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/ls/>।

- বর্তমানে চলমান Docker কন্টেইনারগুলো তালিকাভুক্ত করুন:

`docker {{[ps|container ls]}}`

- সমস্ত Docker কন্টেইনার তালিকাভুক্ত করুন (চলমান এবং বন্ধ):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- সর্বশেষ তৈরি হওয়া কন্টেইনার দেখান (সব অবস্থা অন্তর্ভুক্ত):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- নামে একটি সাবস্ট্রিং থাকা কন্টেইনারগুলো ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{name}}"`

- নির্দিষ্ট একটি ইমেজকে পূর্বসূরি হিসেবে থাকা কন্টেইনারগুলো ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- প্রস্থান (exit) স্ট্যাটাস কোড অনুযায়ী কন্টেইনারগুলো ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "exited={{code}}" {{[-a|--all]}}`

- অবস্থা অনুযায়ী কন্টেইনারগুলো ফিল্টার করুন (created, running, removing, paused, exited, এবং dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- নির্দিষ্ট একটি ভলিউম মাউন্ট করা বা নির্দিষ্ট পথে ভলিউম মাউন্ট থাকা কন্টেইনারগুলো ফিল্টার করুন:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
