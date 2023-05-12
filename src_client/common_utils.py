import os
from src_core.processing_configuration.config_utils import GLOBAL_CONFIG, build_config_file_name
from basic.log.logger2 import service_logger, LoggingContext, name_and_args
from src_core.processing_configuration.configuration import configs_folder_name

service_logger = service_logger()

def process_files(client, data_root, period, smart_csv=False, configuration_xlsx=None, chunk_size=None,
                  config_source=GLOBAL_CONFIG, excel_force_printable=False, excel_skip_hidden_sheets=False,
                  template_ignore_case=False, excel_header_finder=False, smart_footer=None, smart_header=None,
                  process_with_unmatched=False, column_order=None, new_columns=None, check_on_pii=None,
                  replace_pii_row = True, replace_whitespaces = False):
    LoggingContext.Client = client
    service_logger.info(f'Function: {process_files.__name__}, Args: {name_and_args()}')
    if configuration_xlsx is None:
        config_basename = build_config_file_name(client)
        configuration_xlsx = os.path.join(configs_folder_name, config_basename)
        service_logger.info(configuration_xlsx)



if __name__ == "__main__":
    input_folder = r"C:\LHARC\my\_R2.14\PII_Recognizer\Abc_xlsx_csv"
    period = '2019Q4'
    client = 'abc'
    print(__file__)
    process_files(client, input_folder, period, config_source='local')
