# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:12:15 2020

@author: diogo
"""

from exif import Image
import os
import shutil

#antes de achatar a arvore, tenho que extrair os metadados, eles não são copiados juntos. Arquivos\129.jpg
#D:\Sistema\Arquivos de Usuário\Projetos\Projeto Criptografia\Arquivos\5.jpg 'IMG_20151227_163601.jpg'


#vou ver se todas as imagens estão sem metadados

def ExtractMetadata(folder):

    rprt = open("Report" + folder,'w')

    for root, dirpath, files in os.walk(folder):
        for names in files:
            ext = os.path.splitext(names)[1]
            if ext==".jpg":
                with open('Arquivos\\129.jpg', 'rb') as image_file:
                    my_image = Image(image_file)

                    rprt.write(names + " - ")
                    rprt.write(str(my_image.has_exif)+ " - ")
                    rprt.write(str(dir(my_image)))
                    rprt.write('\n')
    rprt.close()

ExtractMetadata('Arquivos Originais')
