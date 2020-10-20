# Extract Arduino Hashtagged Tweets

## Component Overview
Event Bridge -> Tweet Mine Lambda -> SQS
SQS -> Tweet Transform Lambda -> DynamoDB
API -> Tweet API <- DynamoDB

## Lambdas
### Tweet Mine
#### First time packaging up the project
See: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
#### How to Update
`zip twitter.zip lambda_function.py`
`aws lambda update-function-code --function-name twitter_mine --zip-file fileb://twitter.zip --profile`
#### Change Alias of Prod
`aws lambda update-alias --function-name twitter_mine --name prod --function-version 2 --profile`
`aws lambda update-alias --function-name ArduinoTweetParser --name prod --function-version 2 --profile`

### UserTweets
#### Create
`zip user_tweets.zip lambda_function.py`
`aws lambda create-function --function-name ArduinoUserTweets --runtime python3.8 --role arn:aws:iam::575798484766:role/goPizza-ExecuteLambdaRole-4L1Z64KBS8XL --handler lambda_function.lambda_handler --zip-file=fileb://user_tweets.zip --profile`

#### Delete
`aws lambda delete-function  --function-name ArduinoUserTweets --profile`

### Update Code
`zip user_tweets.zip lambda_function.py`
`aws lambda update-function-code --function-name ArduinoUserTweets --zip-file fileb://user_tweets.zip --profile`

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