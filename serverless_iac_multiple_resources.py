# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'provider': {'name': 'learning-serverless', 'runtime': 'python3.8', 'stage': 'dev', 'region': 'us-east-1', 'iamRoleStatements': {'Effect': 'Allow', 'Action': ['s3:GetObject', 's3:PutObject'], 'Resource': 'arn:aws:s3:::Learning-Serverless-*'}}}