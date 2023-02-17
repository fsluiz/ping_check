import os
import time

with open('host.txt') as file:
    dump = file.read() # lê o arquvio
    dump = dump.splitlines()# coloca em linhas separadas
    
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' *60)# imprime '-' 60 vezes
        os.system('ping -n 2 {}'.format(ip))
        print('-' *60)
        time.sleep(5)# faz uma espera de 5 segundo entre uma execução e outra. 