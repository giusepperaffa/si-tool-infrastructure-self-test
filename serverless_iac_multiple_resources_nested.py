# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'serverless-ruby-sqs-dynamodb', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'ruby2.7', 'memorySize': 256, 'lambdaHashingVersion': 20201221, 'iam': {'role': {'statements': [{'Effect': 'Allow', 'Action': ['s3:GetObject', 's3:PutObject'], 'Resource': ['arn:aws:s3:::Learning-Serverless-*']}]}}}, 'constructs': {'lotteryQueue': {'type': 'queue', 'worker': {'handler': 'src/handlers/lottery/worker.run', 'environment': {'TABLE_NAME': '${self:custom.tableName}'}}, 'alarm': '${self:custom.alertEmail}', 'batchSize': 5}}}