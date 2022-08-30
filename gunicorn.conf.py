import os
from dotenv import load_dotenv

load_dotenv()

bind = '0.0.0.0:{}'.format(os.getenv('PORT', 8000))
workers = 2
