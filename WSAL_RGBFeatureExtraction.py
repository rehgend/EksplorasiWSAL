import os                                     #Module untuk manajemen file
import sys                                    #Module untuk mengakses program dan menjalankan file kode python di lingkungan direktori atau sistem itu sendiri
import numpy as np                            #Module yang digunakan untuk komputasi ilmiah dan pekerjaan yang melibatkan data array
import cv2                                    #Module untuk memanfaatkan open source computer vision atau yang dikenal dengan openCV
from multiprocessing import Pool              #Kelas modul yang dapat menangani sejumlah besar proses, sehingga dapat membuat jalannya multiple jobs per-process
from multiprocessing import current_process   #Kelas modul yang mampu membantu menginfokan process object yang terdapat pada proses saat ini
from multiprocessing import freeze_support    #Kelas modul yang mampu menghentikan (freeze) ketika suatu program menggunakan multiprocessing

#Proses mengunduh dataset dari kaggle terkait dengan sample UCF Crime (Dilakukan Cukup Satu Kali)
#import opendatasets as od
#od.download("https://www.kaggle.com/datasets/mission-ai/crimeucfdataset")

from tensorflow.python.platform import build_info as tf_build_info