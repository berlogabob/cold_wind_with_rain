# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cell_v = [-0.25, -0.239999994635582, -0.230000004172325, -0.219999998807907, -0.209999993443489, -0.200000002980232, -0.189999997615814, -0.180000007152557, -0.170000001788139, -0.159999996423721, -0.150000005960464, -0.140000000596046, -0.129999995231628, -0.119999997317791, -0.109999999403954, -0.100000001490116, -0.0900000035762787, -0.0799999982118607, -0.0700000002980232, -0.0599999986588955, -0.0500000007450581, -0.0399999991059303, -0.0299999993294477, -0.0199999995529652, -0.00999999977648258, 0, 0.00999999977648258, 0.0199999995529652, 0.0299999993294477, 0.0399999991059303, 0.0500000007450581, 0.0599999986588955, 0.0700000002980232, 0.0799999982118607, 0.0900000035762787, 0.100000001490116, 0.109999999403954, 0.119999997317791, 0.129999995231628, 0.140000000596046, 0.150000005960464, 0.159999996423721, 0.170000001788139, 0.180000007152557, 0.189999997615814, 0.200000002980232, 0.209999993443489, 0.219999998807907, 0.230000004172325, 0.239999994635582, 0.25, 0.259999990463257, 0.270000010728836, 0.280000001192093, 0.28999999165535, 0.300000011920929, 0.310000002384186, 0.319999992847443, 0.330000013113022, 0.340000003576279, 0.349999994039536, 0.360000014305115, 0.370000004768372, 0.379999995231628, 0.389999985694885, 0.400000005960464, 0.409999996423721, 0.419999986886978, 0.430000007152557, 0.439999997615814, 0.449999988079071, 0.46000000834465, 0.469999998807907, 0.479999989271164, 0.490000009536743, 0.5, 0.5, 0.490000009536743, 0.479999989271164, 0.469999998807907, 0.46000000834465, 0.449999988079071, 0.439999997615814, 0.430000007152557, 0.419999986886978, 0.409999996423721, 0.400000005960464, 0.389999985694885, 0.379999995231628, 0.370000004768372, 0.360000014305115, 0.349999994039536, 0.340000003576279, 0.330000013113022, 0.319999992847443, 0.310000002384186, 0.300000011920929, 0.28999999165535, 0.280000001192093, 0.270000010728836, 0.259999990463257, 0.25, 0.239999994635582, 0.230000004172325, 0.219999998807907, 0.209999993443489, 0.200000002980232, 0.189999997615814, 0.180000007152557, 0.170000001788139, 0.159999996423721, 0.150000005960464, 0.140000000596046, 0.129999995231628, 0.119999997317791, 0.109999999403954, 0.100000001490116, 0.0900000035762787, 0.0799999982118607, 0.0700000002980232, 0.0599999986588955, 0.0500000007450581, 0.0399999991059303, 0.0299999993294477, 0.0199999995529652, 0.00999999977648258, 0, -0.00999999977648258, -0.0199999995529652, -0.0299999993294477, -0.0399999991059303, -0.0500000007450581, -0.0599999986588955, -0.0700000002980232, -0.0799999982118607, -0.0900000035762787, -0.100000001490116, -0.109999999403954, -0.119999997317791, -0.129999995231628, -0.140000000596046, -0.150000005960464, -0.159999996423721, -0.170000001788139, -0.180000007152557, -0.189999997615814, -0.200000002980232, -0.209999993443489, -0.219999998807907, -0.230000004172325, -0.239999994635582, -0.25]

cell_gel_i = [-5.28119E-06, -4.88329E-06, -4.4915E-06, -4.09948E-06, -3.71974E-06, -3.35676E-06, -3.01471E-06, -2.69501E-06, -2.40201E-06, -2.13564E-06, -1.89096E-06, -1.66984E-06, -1.46929E-06, -1.29029E-06, -1.13187E-06, -9.95287E-07, -8.65814E-07, -7.43823E-07, -6.35074E-07, -5.35246E-07, -4.45426E-07, -3.64203E-07, -2.905E-07, -2.27097E-07, -1.66639E-07, -1.13993E-07, -6.63869E-08, -2.39295E-08, 1.17388E-08, 4.58264E-08, 7.62762E-08, 1.02634E-07, 1.27584E-07, 1.49403E-07, 1.69519E-07, 1.89303E-07, 2.0716E-07, 2.23222E-07, 2.41365E-07, 2.57541E-07, 2.73887E-07, 2.89637E-07, 3.04866E-07, 3.22376E-07, 3.37445E-07, 3.55079E-07, 3.71301E-07, 3.8911E-07, 4.06492E-07, 4.26828E-07, 4.48668E-07, 4.72365E-07, 5.00189E-07, 5.33164E-07, 5.73851E-07, 6.24015E-07, 6.87279E-07, 7.66047E-07, 8.66806E-07, 9.85064E-07, 1.00855E-06, 1.17881E-06, 1.36565E-06, 1.57011E-06, 1.78348E-06, 2.00174E-06, 2.22087E-06, 2.43387E-06, 2.64129E-06, 2.83157E-06, 3.00636E-06, 3.1664E-06, 3.30353E-06, 3.42141E-06, 3.52328E-06, 3.60924E-06, 5.20435E-07, 4.9883E-07, 4.78905E-07, 4.54014E-07, 4.28814E-07, 4.00848E-07, 3.70358E-07, 3.3864E-07, 3.02753E-07, 2.72903E-07, 2.28768E-07, 1.90389E-07, 1.56515E-07, 1.19977E-07, 8.3309E-08, 5.56137E-08, 2.82809E-08, 4.65855E-09, -8.6401E-09, -1.99875E-08, -3.05312E-08, -3.7629E-08, -4.22131E-08, -4.50473E-08, -4.61232E-08, -4.80316E-08, -4.89193E-08, -5.14082E-08, -5.01777E-08, -5.21513E-08, -5.2191E-08, -5.46156E-08, -5.61432E-08, -5.86997E-08, -5.85702E-08, -6.23775E-08, -6.4956E-08, -6.80611E-08, -7.24376E-08, -7.70754E-08, -8.00752E-08, -8.37112E-08, -9.0449E-08, -9.82003E-08, -1.0365E-07, -1.12495E-07, -1.22338E-07, -1.32997E-07, -1.45713E-07, -1.60741E-07, -1.76468E-07, -1.94712E-07, -2.16163E-07, -2.40799E-07, -2.68524E-07, -2.99978E-07, -3.356E-07, -3.72764E-07, -4.16781E-07, -4.66459E-07, -5.20605E-07, -5.79602E-07, -6.44033E-07, -7.16328E-07, -7.92953E-07, -8.75486E-07, -9.65401E-07, -1.0473E-06, -1.14825E-06, -1.2546E-06, -1.36616E-06, -1.48156E-06, -1.60264E-06, -1.72921E-06, -1.85958E-06, -1.99438E-06]

cell_no_gel = [-3.25483E-06, -2.95466E-06, -2.67678E-06, -2.41908E-06, -2.18421E-06, -1.97318E-06, -1.77388E-06, -1.6062E-06, -1.43972E-06, -1.29376E-06, -1.15867E-06, -1.04079E-06, -9.31814E-07, -8.22841E-07, -7.27464E-07, -6.4078E-07, -5.57918E-07, -4.81796E-07, -4.09483E-07, -3.46469E-07, -2.88708E-07, -2.33417E-07, -1.84733E-07, -1.3287E-07, -1.01754E-07, -6.35968E-08, -3.95458E-08, -5.32816E-09, 1.96249E-08, 3.56193E-08, 6.2844E-08, 8.46752E-08, 9.00183E-08, 1.11689E-07, 1.27949E-07, 1.39374E-07, 1.53882E-07, 1.63578E-07, 1.74793E-07, 1.80213E-07, 1.96831E-07, 2.07811E-07, 2.18729E-07, 2.29478E-07, 2.37841E-07, 2.50474E-07, 2.63801E-07, 2.78207E-07, 2.87243E-07, 3.02592E-07, 3.16786E-07, 3.34366E-07, 3.64363E-07, 3.94852E-07, 4.31927E-07, 4.84557E-07, 5.3415E-07, 6.16655E-07, 7.00322E-07, 7.9802E-07, 9.00438E-07, 1.01689E-06, 1.03333E-06, 1.15613E-06, 1.27961E-06, 1.39316E-06, 1.50312E-06, 1.60209E-06, 1.69228E-06, 1.77747E-06, 1.85809E-06, 1.92103E-06, 1.97007E-06, 2.02935E-06, 2.07281E-06, 2.11594E-06, 5.54036E-07, 5.41142E-07, 5.1973E-07, 5.06061E-07, 4.89666E-07, 4.69923E-07, 4.60164E-07, 4.25254E-07, 4.00466E-07, 3.7271E-07, 3.3446E-07, 2.99004E-07, 2.67429E-07, 2.21551E-07, 1.77258E-07, 1.36114E-07, 9.3365E-08, 6.155E-08, 3.49655E-08, 1.28185E-08, -9.09911E-09, -2.53725E-08, -3.54158E-08, -4.29303E-08, -4.86047E-08, -5.13053E-08, -7.32263E-08, -5.49078E-08, -5.62113E-08, -6.14292E-08, -7.56762E-08, -7.44884E-08, -6.99602E-08, -7.83129E-08, -7.11002E-08, -8.84671E-08, -8.87985E-08, -9.16438E-08, -9.916E-08, -1.1064E-07, -1.11364E-07, -1.20483E-07, -1.29277E-07, -1.36139E-07, -1.55271E-07, -1.59958E-07, -1.70724E-07, -1.87947E-07, -2.10431E-07, -2.21544E-07, -2.31689E-07, -2.74416E-07, -2.9296E-07, -3.20129E-07, -3.51345E-07, -3.89922E-07, -4.2713E-07, -4.68824E-07, -5.1272E-07, -5.65376E-07, -6.2993E-07, -6.89704E-07, -7.63172E-07, -8.42584E-07, -9.1187E-07, -9.99664E-07, -1.08346E-06, -1.17912E-06, -1.28714E-06, -1.40353E-06, -1.51885E-06, -1.64319E-06, -1.77171E-06, -1.90026E-06, -2.04163E-06, -2.18128E-06]

plt.figure(num = 1, figsize=(10,6), dpi= 600)
#plt.suptitle("usinp_title", fontsize=16)
plt.plot(cell_v, cell_gel_i, "b", cell_v, cell_no_gel, "r")
#plt.plot(cell_v, cell_no_gel, "r")

plt.xlabel('millivolt')
plt.ylabel('microampere')
plt.grid(True)
#вывод
plt.figure(1).savefig("20170410" + 'e' + '.png')
plt.figure(1).savefig("20170410" + 'e' + '.pdf')
plt.show()
