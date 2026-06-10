# redis- հենանիշ

> Հենանիշ Redis սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>:.

- Գործարկել ամբողջական չափանիշը.:

`redis-benchmark`

- Գործարկել հենանիշը կոնկրետ Redis սերվերի վրա.:

`redis-benchmark -h {{host}} -p {{port}} -a {{password}}`

- Գործարկեք թեստերի ենթաբազմություն լռելյայն 100000 հարցումներով.:

`redis-benchmark -h {{host}} -p {{port}} -t {{set,lpush}} -n {{100000}}`

- Գործարկել կոնկրետ սցենարով.:

`redis-benchmark -n {{100000}} script load "{{redis.call('set', 'foo', 'bar')}}"`

- Գործարկել հենանիշը՝ օգտագործելով 100000 [r] պատահական ստեղներ.:

`redis-benchmark -t {{set}} -r {{100000}}`

- Գործարկել հենանիշը՝ օգտագործելով 16 հրամանների [P]ipelining.:

`redis-benchmark -n {{1000000}} -t {{set,get}} -P {{16}}`

- Հանգիստ գործարկեք հենանիշը [q] և ցուցադրեք միայն հարցումը մեկ վայրկյանում արդյունք.:

`redis-benchmark -q`
