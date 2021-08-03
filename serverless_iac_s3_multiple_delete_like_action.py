# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'provider': {'name': 'learning-serverless', 'runtime': 'python3.8', 'stage': 'dev', 'region': 'us-east-1', 'iamRoleStatements': {'Effect': 'Allow', 'Action': ['s3:DeleteObject', 's3:DeleteObjectTagging'], 'Resource': 'arn:aws:s3:::mybucket'}}}