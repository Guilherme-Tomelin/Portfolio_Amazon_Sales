import unicodedata
import re
from src.config.logger_settings import LoggerConfig
from datetime import datetime

def instantitate_logs():
    log_config = LoggerConfig()
    log_config.setup_console_logging()  
    log_config.setup_file_logging()
    logger = log_config.get_logger()
    return logger

def process_dictionary_data(dictionary: dict) -> dict:
    def process_text(text: str) -> str:
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        
        def replace_non_alphanumeric_except_slash(match):
            if re.match(r'\d+/\d+', match.group(0)):  
                return match.group(0)  
            return re.sub(r'\W+', '_', match.group(0))  

        text = re.sub(r'[^\w/]+|(?<!\d)/|/(?!\d)', replace_non_alphanumeric_except_slash, text)
        
        return text.lower()

    return {process_text(k): process_text(v) if isinstance(v, str) else v for k, v in dictionary.items()}

def convert_to_date(value: str):
    try:
        return datetime.strptime(value, '%d/%m/%Y').date()
    except ValueError:
        return value
    
