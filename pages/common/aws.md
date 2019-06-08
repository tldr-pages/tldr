# aws

> The official CLI tool for Amazon Web Services.
> More information: <https://aws.amazon.com/cli>.

- List all IAM users:

`aws iam list-users`

- List all EC2 instances from a specific region:

`aws ec2 describe-instances --region {{us-east-1}}`

- Receive message from a specific SQS queue:

`aws sqs receive-message --queue-url {{https://queue.amazonaws.com/546123/Test}}`

- Publish message to the specific SNS topic:

`aws sns publish --topic-arn {{arn:aws:sns:us-east-1:54633:testTopic}} --message "Message"`

- To see help text for the AWS command:

`aws {{command}} help`
