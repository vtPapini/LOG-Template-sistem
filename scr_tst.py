import logging_profile as lg 
from logging_profile import logging


###########################
#Configurando LOG
###########################

lg.Log_config('Test')

while lg.errors_total != 2:
    logging.error("Simulacao de ERRO")
    logging.info("Simulacao de ERRO")

print("Number of Errors ", lg.errors_total)
