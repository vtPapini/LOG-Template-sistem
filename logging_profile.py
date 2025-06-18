import logging
from datetime import datetime


###########################################################
# LOG SETUP
###########################################################
# Contagem de erro
errors_total = 0


# Função customizada de erro
def custom_error(self, msg, *args, **kwargs):
    global errors_total
    errors_total += 1  # Increment error count
    self._log(logging.ERROR, msg, args, **kwargs)

# Log Config

#-----------Log File config
def Log_config(name_log_prefix: str, delimiter = "|", _custom_error = custom_error):
    """
    Parameters
    ----------
    name_log_prefix : str
        Prefix used to define the name of log_file.
            
    delimiter : str
        Delimiter of file and console logging.Formatter.
    
    Summary
    -----

    `log_file:` fr"{`name_log_prefix`}-log_{datetime.today().strftime('%Y_%m_%d')}.log"

    `file_formatter:` f"%(asctime)s {delimiter} %(levelno)s {delimiter} %(levelname)s {delimiter} %(message)s"

    `console_formatter:` f"%(levelname)s {delimiter} %(message)s"
    
    """

    log_file = fr"{name_log_prefix}-log_{datetime.today().strftime('%Y_%m_%d')}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_formatter = logging.Formatter(f"%(asctime)s{delimiter}%(levelno)s{delimiter}%(levelname)s{delimiter}%(message)s")
    console_formatter = logging.Formatter(f"%(levelname)s {delimiter} %(message)s")

    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logging.Logger.error = _custom_error

#############
#TESTE
#############
# if __name__ == '__main__':
#     #main()
#     Log_config('teste')
#     while errors_total != 5:
#         logging.error("TESTE message")
#     print(errors_total)


#################################################################
############# Exemplo de configuração de importação
#################################################################

# import logging_tst as lg 
# from logging_tst import logging


# ###########################
# #Configurando LOG
# ###########################

# lg.Log_config('Test')

# while lg.errors_total != 2:
#     logging.error("Simulacao de ERRO")
#     logging.info("Simulacao de ERRO")

# print("Number of Errors ", lg.errors_total)