# Extract Arduino Hashtagged Tweets

## Component Overview
Event Bridge -> Tweet Mine Lambda -> SQS
SQS -> Tweet Transform Lambda -> DynamoDB
API -> Tweet API <- DynamoDB

## AWS Stacks Used
### Lambda
For the retrieval and processing of data
1. tweet mine
2. arduino tweet parser
### Event Bridge
Invokes the `tweet mine` lambda to kick things off
### SQS
Bridging the different lambdas
1. enqueue-encrypted: contains all the messages
### DynamoDB
*arduino_tweets*: Storing the tweets