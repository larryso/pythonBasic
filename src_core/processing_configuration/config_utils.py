from src_core.processing_configuration.excel_config import CONFIG_FILE_POSTFIX, CONFIG_FILE_EXTENSION

CONFIG_DIR_NAME = 'config'
GLOBAL_CONFIG = 'global'
LOCAL_CONFIG = 'local'

def build_config_file_name(*name_parts: str, postfix: str = CONFIG_FILE_POSTFIX,
                           extension: str = CONFIG_FILE_EXTENSION) -> str:
    return '_'.join(name_parts) + postfix + extension
