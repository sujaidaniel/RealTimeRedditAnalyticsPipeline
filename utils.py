import configparser
import os

# Initialize the configuration parser and read the configuration file
config_parser = configparser.ConfigParser()
config_parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

# API Keys for Reddit
REDDIT_SECRET_KEY = config_parser.get('api_keys', 'reddit_secret_key')
REDDIT_CLIENT_ID = config_parser.get('api_keys', 'reddit_client_id')

# Database credentials and configuration
DB_HOST = config_parser.get('database', 'database_host')
DB_NAME = config_parser.get('database', 'database_name')
DB_PORT = config_parser.get('database', 'database_port')
DB_USER = config_parser.get('database', 'database_username')
DB_PASSWORD = config_parser.get('database', 'database_password')

# AWS Credentials and configuration
AWS_ACCESS_KEY_ID = config_parser.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config_parser.get('aws', 'aws_secret_access_key')
AWS_REGION = config_parser.get('aws', 'aws_region')
A
