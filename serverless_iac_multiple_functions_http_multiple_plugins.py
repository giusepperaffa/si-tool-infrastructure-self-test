# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'serverless-telegram-bot', 'provider': {'name': 'aws', 'runtime': 'python3.6', 'profile': 'ckl', 'environment': {'TELEGRAM_TOKEN': "${file(./serverless.env.yml):TELEGRAM_TOKEN, ''}"}}, 'functions': {'webhook': {'handler': 'handler.webhook', 'events': [{'http': 'POST /'}]}, 'set_webhook': {'handler': 'handler.set_webhook', 'events': [{'http': 'POST /set_webhook'}]}}, 'plugins': ['serverless-ruby-layer', 'serverless-lift']}