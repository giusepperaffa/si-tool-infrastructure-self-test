# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-rust-simple-http-endpoint', 'plugins': ['serverless-rust'], 'functions': {'test_test': {'handler': 'test', 'events': [{'http': {'path': 'test/test', 'method': 'get'}}]}}}