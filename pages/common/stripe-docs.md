# stripe docs

> Browse docs.stripe.com from the terminal.
> More information: <https://docs.stripe.com/cli/docs>.

- Read a documentation page by path:

`stripe docs {{/payments}}`

- Read an API reference page by resource name:

`stripe docs api {{product}}`

- Read an API reference page by HTTP method and path:

`stripe docs api {{GET /v1/products}}`

- Read an API reference page for a webhook event:

`stripe docs api {{product.created}}`

- Search documentation by keywords:

`stripe docs search "{{payment intents}}"`
