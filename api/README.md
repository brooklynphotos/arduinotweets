# API Gateway
## Importing
`aws apigateway import-rest-api --body 'file://api/swagger.json' --fail-on-warnings --profile`
After a gateway is created an API ID is generated and will be used in all the commands below
## Removing
`aws apigateway delete-rest-api --rest-api-id gu82d61gji --profile`

## Deploying
### Create a New Deployment
`aws apigateway create-deployment --region eu-west-1 --rest-api-id 5z5xpa1hrd --stage-name dev --variables stage=dev --profile`
### Deploying using existing deployment
`aws apigateway update-stage --region eu-west-1 --rest-api-id <rest-api-id>  --stage-name dev  --patch-operations op='replace',path='/deploymentId',value='<deployment-id>'`

## Grant Permission to Use Lambda
`aws lambda add-permission --function-name ArduinoTweetViewer --action lambda:InvokeFunction --statement-id get_user_invoke_ArduinoTweetViewer --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users/* --output text --profile`
`aws lambda add-permission --function-name ArduinoTweetViewer --action lambda:InvokeFunction --statement-id get_users_invoke_ArduinoTweetViewer --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users --output text --profile`
`aws lambda add-permission --function-name "arn:aws:lambda:eu-west-1:575798484766:function:ArduinoUserTweets:dev" --action lambda:InvokeFunction --statement-id get_user_tweets_invoke_ArduinoUserTweets --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:eu-west-1:575798484766:5z5xpa1hrd/*/GET/users/*/tweets --output text --profile`