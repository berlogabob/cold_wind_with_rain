# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
07102016-2.dat

14102016-1.dat

14102016-2.dat

"""
usinp = "20170407_sum.csv"
#usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
usinp_e = usinp[0:-4] + 'e' + usinp[-4:len_usinp]
#print usinp_e
#название файла без разширения, для отображения на граффике
usinp_title = usinp[0:-4]
#
s = open(usinp).read()#прочитали исходный файл
"""
#блок замен
s = s.replace('"', '')#удаляем кавычки
s = s.replace('sec', '"sec"')#удаляем кавычки
s = s.replace('mA', '"mA"')#удаляем кавычки
s = s.replace('mV', '"mV"')#удаляем кавычки
s = s.replace('    ', '\t')#меняем запятую на точкуу
s = s.replace(',', '.')#меняем запятую на точкуу
#s = s.replace('\n', ', ')#замена новой строки на запятую
#s = s.replace(',', '\t')#замена запятой символом табуляции
#s = s.replace('.', ',')#замена точки заятой
"""
#создаем новый файл для записывания в него изменений
f = open(usinp_e, 'w')#открыли файл (создали)
f.write(s)#записали
f.close()#закрыли

#создаем датафрэйм
frame = pd.read_csv(usinp_e, sep = ";")

allarray = np.array(frame)

#Item = np.array(frame["Item"])
#Smu1_V = np.array(frame["Smu1_V"])
#Smu1_I = np.array(frame["Smu1_I"])
#Smu1_R = np.array(frame["Smu1_R"])
#Smu1_Time = np.array(frame["Smu1_Time"])
"""
#зона вывода графф
plt.figure(num = 1, figsize=(10,6), dpi= 150)
plt.suptitle(usinp_title, fontsize=16)
plt.subplots_adjust(hspace=0.4)#
#первый графф
plt.subplot(2,1,1)
plt.plot(Smu1_V, Smu1_I)
plt.xlabel('Smu1_V, mV')
plt.ylabel('Smu1_I, mA')
#plt.title(u'Изменение тока по времени', fontsize=12)
#plt.grid(True)
"""
"""
#второй графф
plt.subplot(2,1,2)
plt.plot(mv, ma, '-r')
plt.xlabel('Volts, mV')
plt.ylabel('I, mA')
plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
"""
"""
#вывод
plt.figure(1).savefig(usinp_title + 'e' + '.png')
plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
plt.show()
"""
print allarray
