# -*- coding: utf-8 -*-
"""
@author: diogo
"""

#O objetivo arquivos de uma pasta, e apontar quais não são iguais.
#Como esse código vai ser um rotina de um outro maior não preciso comparar um com todos,
#vou selecionar por nomes, vistos que eles devem ser 'xarás' só estarão salvos em pastas diferentes.

import filecmp
#Função para comparar e reportar o q achou.
def Verificador(origem, dcrpt):
    
    cmp = filecmp.dircmp(origem, dcrpt, ignore=None, hide=None)

    frprt = open("f Report",'w')
    drprt = open("d Report",'w')
    srprt = open("s Report",'w')

    for name in cmp.funny_files:
        frprt.write(name)

    for name in cmp.diff_files:
        drprt.write(name)

    for name in cmp.same_files:
        srprt.write(name)

    frprt.close()
    drprt.close()
    srprt.close()

Verificador('Arquivos', 'ArquivosDcrpt')