# API Gateway
## Importing
`aws apigateway import-rest-api --body 'file://api/swagger.json' --fail-on-warnings --profile`
## Removing
`aws apigateway delete-rest-api --rest-api-id gu82d61gji --profile`

## Deploying
`aws apigateway create-deployment --region eu-west-1 --rest-api-id 5z5xpa1hrd --stage-name dev --profile`

## Grant Permission to Use Lambda
`aws lambda add-permission --function-name ArduinoTweetViewer --action lambda:InvokeFunction --statement-id get_user_invoke_ArduinoTweetViewer --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users/* --output text --profile`
`aws lambda add-permission --function-name ArduinoTweetViewer --action lambda:InvokeFunction --statement-id get_users_invoke_ArduinoTweetViewer --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users --output text --profile`
`aws lambda add-permission --function-name ArduinoUserTweets --action lambda:InvokeFunction --statement-id get_user_tweets_invoke_ArduinoUserTweets --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users/*/tweets --output text --profile`