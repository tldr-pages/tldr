# wait4x

> Lightweight, zero-dependency tool to wait for services to be ready.
> Perfect for CI/CD pipelines, containers, and local development.
> More information: <https://wait4x.dev>.

- Wait for a PostgreSQL database to be ready on a specific host and port:

`wait4x postgresql --host {{localhost}} --port {{5432}}`

- Wait for an HTTP endpoint to respond successfully (e.g., status 200):

`wait4x http --url {{http://localhost:8080/health}}`

- Wait for a Redis server to be ready with a 30-second timeout:

`wait4x redis --host {{redis}} --port {{6379}} --timeout {{30s}}`

- Wait for a TCP service to become available on a given host and port:

`wait4x tcp --host {{example.com}} --port {{8080}}`

- Wait for a DNS record to resolve:

`wait4x dns --host {{example.com}}`

- Wait for a RabbitMQ broker to be available:

`wait4x rabbitmq --host {{rabbitmq}} --port {{5672}}`

- Wait for a MongoDB instance to become available:

`wait4x mongodb --host {{localhost}} --port {{27017}}`

- Wait for a Kafka broker to start accepting connections:

`wait4x kafka --host {{localhost}} --port {{9092}}`
