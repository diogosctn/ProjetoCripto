# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:32:50 2020

@author: diogo
"""

#Primeira Etapa: Entrar nos diretórios.

strtest = "Teste";

testeorigem = open("Teste Diretório Original\TesteOrigem.txt","a")
testedestino = open("Teste Diretório Destino\TesteDestino.txt","a")

testeorigem.write(strtest);
testedestino.write(strtest);

testeorigem.close();
testedestino.close();

#Segunda Etapa: Verificar se é arquivo ou diretório.

import os

folder = 'Teste Diretório Original'
folder = 'Arquivos Originais'
filepaths = [f.path for f in os.scandir(folder) if f.is_file()]
dirpaths  = [f.path for f in os.scandir(folder) if f.is_dir()]


for = os.scandir(folder); 
    print(f.is_file());


def Verificador(path):

    for f in os.scandir(path):
        if f.is_file(): 
            print(f.path + ' é um arquivo');
            
        elif f.is_dir(): 
            print(f.path + ' é um diretório');
            
Verificador(folder)


#Terceira Etapa: Criar processo iterativo.

import os
import shutil

def FlattenTree(origem, destino):

    count = 1    
    for root, dirpath, files in os.walk(origem):
        for names in files:
            ext = os.path.splitext(names)[1]
            shutil.copy2(os.path.join(root, names),destino  + "\\" + str(count) + ext)
            count = count + 1;


foldero = 'Arquivos Originais'
folderd = 'Arquivos'

FlattenTree(foldero,folderd)

# A princípio pensei em criar um processo iterativo que verificava pasta por pasta, mas depois descobri que é 
#possível fazer isso de forma muito mais simples usando o 'os.walk()'.
#Ele verifica tudo dentro de uma arvore de arquivos, dessa forma fica muito mais fácil pegar os arquivos.
