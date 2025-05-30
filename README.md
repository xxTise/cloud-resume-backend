📁 Cloud Resume Challenge (Backend)

This is the backend repository for my Cloud Resume Challenge project. It powers the visitor count displayed on the static resume by using AWS Lambda, API Gateway, and DynamoDB.

⚖️ Tech Stack / Tools Used

AWS Lambda (Python backend)

Amazon DynamoDB (Stores visitor count)

API Gateway (Triggers Lambda)

AWS SAM (Serverless Application Model) (Infrastructure as Code)

GitHub Actions (CI/CD pipeline)


🎮 API Endpoint
GET https://wr7nssjxka.execute-api.us-east-1.amazonaws.com/updatevisitorcount
Returns:
{
  "visit_count": 13
}


⚙️ How It Works

API Gateway exposes a REST endpoint.

A Lambda function is triggered.

Lambda increments and reads from a DynamoDB table VisitorCount.

It returns the updated count to frontend.


🚀 Deployment Steps

1. Manual SAM Deployment (locally)

sam build
sam deploy --guided

2. GitHub Actions CI/CD

This repo contains a workflow that automatically builds and deploys your Lambda using SAM when changes are pushed.

 name: Deploy Backend
  on:
    push:
      branches: [main]

  jobs:
    build-and-deploy:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2

        -  name: Install AWS SAM CLI
          run: |
            pip install aws-sam-cli

        - name: Build SAM
          run: sam build

        - name: Deploy SAM
          run: >
            sam deploy --no-confirm-changeset --no-fail-on-empty-changeset \
            --stack-name cloud-resume-backend --capabilities CAPABILITY_IAM
          env:
            AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
            AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
            AWS_REGION: 'us-east-1'

 
 🛠️ Notable Challenges

AccessDenied on Lambda — Resolved by updating IAM role with necessary Lambda + DynamoDB permissions.

Decimal Serialization Error — Resolved by casting Decimal to int in Python.

ResourceNotFoundException — Solved by ensuring VisitorCount table exists and matches the code.

✨ Outcome

Fully automated backend powering visitor metrics

Solid experience using SAM, Lambda, DynamoDB, and API Gateway

CI/CD pipeline via GitHub Actions for reliable deployments






