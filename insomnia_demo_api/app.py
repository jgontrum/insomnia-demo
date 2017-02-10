import logging

import logstash
import connexion

from insomnia_demo_api import options

logging.basicConfig(level=logging.INFO)

# Logging configuration
logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logstash_options = options()['logstash']
ls = logstash.TCPLogstashHandler(
    host=logstash_options['host'],
    port=logstash_options['port'])
ls.setLevel(logging.INFO)
logger.addHandler(ls)


app = connexion.App("Insomnia Demo API")
application = app.app
app.add_api("config/api.yml",
            strict_validation=True,
            validate_responses=True)

if __name__ == '__main__':
    app.run(port=8080, server='flask')
