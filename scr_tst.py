import logging_tst as lg 
from logging_tst import logging


###########################
#Configurando LOG
###########################

lg.Log_config('Test')

while lg.errors_total != 2:
    logging.error("Simulacao de ERRO")
    logging.info("Simulacao de ERRO")

print("Number of Errors ", lg.errors_total)