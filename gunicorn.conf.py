import os
from dotenv import load_dotenv

load_dotenv()

bind = f"0.0.0.0:{os.getenv('PORT', 8010)}"
workers = 2
