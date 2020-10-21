# Lambdas
## Tweet Mine
### First time packaging up the project
See: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
### How to Update
`zip twitter.zip lambda_function.py`
`aws lambda update-function-code --function-name twitter_mine --zip-file fileb://twitter.zip --profile`
### Change Alias of Prod
`aws lambda update-alias --function-name twitter_mine --name prod --function-version 2 --profile`
`aws lambda update-alias --function-name ArduinoTweetParser --name prod --function-version 2 --profile`

## UserTweets
### Create
`zip user_tweets.zip lambda_function.py`
`aws lambda create-function --function-name ArduinoUserTweets --runtime python3.8 --role arn:aws:iam::575798484766:role/goPizza-ExecuteLambdaRole-4L1Z64KBS8XL --handler lambda_function.lambda_handler --zip-file=fileb://user_tweets.zip --profile`

### Delete
`aws lambda delete-function  --function-name ArduinoUserTweets --profile`

## Update Code
`zip user_tweets.zip lambda_function.py`
`aws lambda update-function-code --function-name ArduinoUserTweets --zip-file fileb://user_tweets.zip --profile`