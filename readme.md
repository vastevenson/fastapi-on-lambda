### FastApi on Lambda 

This repo shows how to get a FastApi app running on Aws Lambda. 

We use Mangum so that Lambda can find the handler and call the correct endpoints. 

To get Lambda to have access to the external dependencies, we need to create a zip that includes the dependencies. To do this, we have pip download the dependencies to a local project directory. 
Run these commands from the project directory in terminal: 
* `pip3 install -t dep -r requirements.txt`
* `(cd dep; zip ../lambda_artifact.zip -r .)`
* `zip lambda_artifact.zip -u main.py`
* Upload the .zip file to Lambda from the Aws Console to a Lambda Function. 
* Make sure that the Lambda function has a Function Url - set it to NONE for authN for testing
* Edit the handler in lambda to `main.handler` - check the CloudWatch Logs to see why it fails. 