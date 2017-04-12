# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import data

#usinp = "data/20170411/20170411-1+1e.csv"
#usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
#len_usinp = len(str(usinp))
#print type(len_usinp)
#usinp_e = usinp[0:-4] + 'e' + usinp[-4:len_usinp]
#print usinp_e
#название файла без разширения, для отображения на граффике
#usinp_title = usinp[0:-4]
#
#s = open(usinp).read()#прочитали исходный файл
#блок замен
#s = s.replace('"', '')#удаляем кавычки
#s = s.replace('sec', '"sec"')#удаляем кавычки
#s = s.replace('mA', '"mA"')#удаляем кавычки
#s = s.replace('mV', '"mV"')#удаляем кавычки
#s = s.replace('    ', '\t')#меняем запятую на точкуу
#s = s.replace(',', '.')#меняем запятую на точкуу
#s = s.replace('\n', ', ')#замена новой строки на запятую
#s = s.replace(',', '\t')#замена запятой символом табуляции
#s = s.replace('.', ',')#замена точки заятой

#создаем новый файл для записывания в него изменений
#f = open(usinp_e, 'w')#открыли файл (создали)
#f.write(s)#записали
#f.close()#закрыли

#создаем датафрэйм
#frame = pd.read_csv(usinp_e, sep = "\t", header = None, names = ['Item', 'Smu1_V(1)(1)', 'Smu1_I(1)(1)', "Smu1_R(1)(1)",'Smu1_Time(1)(1)' ], skiprows = 1)

#allarray = np.array(frame)
#print allarray

Smu1_V_f = "20170411-1+1.csv"
Smu1_V_file = open(Smu1_V_f).read()#прочитали исходный файл
v_frame = pd.read_csv(Smu1_V_file, sep = "\t", header=None, names = ["V"])
print v_frame


"""
"""
"""
#зона вывода графф
plt.figure(num = 1, figsize=(10,6), dpi= 150)
plt.suptitle(usinp_title, fontsize=16)
#plt.subplots_adjust(hspace=0.4)#
#первый графф
#plt.subplot(2,1,1)
plt.plot(Smu1_V, Smu1_I)
plt.xlabel('millivolt')
plt.ylabel('microampere')
#plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
#второй графф

#вывод
plt.figure(1).savefig(usinp_title + 'e' + '.png')
plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
#plt.show()
"""
