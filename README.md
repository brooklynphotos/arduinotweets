# Extract Arduino Hashtagged Tweets

## Component Overview
Event Bridge -> Tweet Mine Lambda -> SQS
SQS -> Tweet Transform Lambda -> DynamoDB
API -> Tweet API <- DynamoDB

## Tweet Mine Lambda
### First time packaging up the project
See: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
### How to Update
`zip twitter.zip lambda_function.py`
`aws lambda update-function-code --function-name twitter_mine --zip-file fileb://twitter.zip --profile`
### Change Alias of Prod
`aws lambda update-alias --function-name twitter_mine --name prod --function-version 2 --profile`
`aws lambda update-alias --function-name ArduinoTweetParser --name prod --function-version 2 --profile`

## API Gateway
### Importing
`aws apigateway import-rest-api --body 'file://api/swagger.json' --fail-on-warnings --profile`
### Removing
`aws apigateway delete-rest-api --rest-api-id gu82d61gji --profile`

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