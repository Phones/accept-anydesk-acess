#!/bin/bash

echo "Ativando o conda"
source ~/.bashrc

echo "Ativa o ambiente conda"
source activate accept-anydesk-acess &>/dev/null

echo "Atualiza o ambiente conda"
pip install -r requirements.txt &>/dev/null

echo "Executa o programa"
python accept_acess.py