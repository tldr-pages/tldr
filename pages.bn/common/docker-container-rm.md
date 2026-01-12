# docker container rm

> কন্টেইনার মুছে ফেলতে ব্যবহৃত হয়।
> আরও তথ্য পাবেন: <https://docs.docker.com/reference/cli/docker/container/rm/>।

- এক বা একাধিক কন্টেইনার মুছে ফেলুন:

`docker {{[rm|container rm]}} {{container1 container2 ...}}`

- জোরপূর্বক একটি কন্টেইনার মুছে ফেলুন:

`docker {{[rm|container rm]}} {{[-f|--force]}} {{container1 container2 ...}}`

- একটি কন্টেইনার এবং তার সাথে যুক্ত ভলিউমসমূহ মুছে ফেলুন:

`docker {{[rm|container rm]}} {{[-v|--volumes]}} {{container}}`

- সাহায্য প্রদর্শন:

`docker {{[rm|container rm]}} {{[-h|--help]}}`
