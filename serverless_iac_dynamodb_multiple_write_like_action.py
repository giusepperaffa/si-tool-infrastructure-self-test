# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'provider': {'name': 'learning-serverless', 'runtime': 'python3.8', 'stage': 'dev', 'region': 'us-east-1', 'iamRoleStatements': {'Effect': 'Allow', 'Action': ['dynamodb:UpdateItem', 'dynamodb:UpdateTable'], 'Resource': 'arn:aws:dynamodb:::table/TABLE_NAME'}}}