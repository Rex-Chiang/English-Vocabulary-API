from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(".").resolve() / ".env"
load_dotenv(dotenv_path)