# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-python-sqs-worker', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'python3.8', 'lambdaHashingVersion': '20201221', 'stage': 'dev'}, 'constructs': {'jobs': {'type': 'queue', 'worker': {'handler': 'handler.consumer'}}}, 'functions': {'producer': {'handler': 'handler.producer', 'events': [{'http': {'method': 'post', 'path': 'produce'}}], 'environment': {'API_KEY': 'api_key'}}}}