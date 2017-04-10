# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cell_v = [-1, -0.990000009536743, -0.980000019073486, -0.970000028610229, -0.959999978542328, -0.949999988079071, -0.939999997615814, -0.930000007152557, -0.920000016689301, -0.910000026226044, -0.899999976158142, -0.889999985694885, -0.879999995231628, -0.870000004768372, -0.860000014305115, -0.850000023841858, -0.839999973773956, -0.829999983310699, -0.819999992847443, -0.810000002384186, -0.800000011920928, -0.790000021457672, -0.779999971389771, -0.769999980926514, -0.759999990463257, -0.75, -0.740000009536743, -0.730000019073486, -0.720000028610229, -0.709999978542328, -0.699999988079071, -0.689999997615814, -0.680000007152557, -0.670000016689301, -0.660000026226044, -0.649999976158142, -0.639999985694885, -0.629999995231628, -0.620000004768372, -0.610000014305115, -0.600000023841858, -0.589999973773956, -0.579999983310699, -0.569999992847443, -0.560000002384186, -0.550000011920928, -0.540000021457672, -0.529999971389771, -0.519999980926514, -0.509999990463257, -0.5, -0.490000009536743, -0.479999989271164, -0.469999998807907, -0.46000000834465, -0.449999988079071, -0.439999997615814, -0.430000007152557, -0.419999986886978, -0.409999996423721, -0.400000005960464, -0.389999985694885, -0.379999995231628, -0.370000004768372, -0.360000014305115, -0.349999994039536, -0.340000003576279, -0.330000013113022, -0.319999992847443, -0.310000002384186, -0.300000011920929, -0.28999999165535, -0.280000001192093, -0.270000010728836, -0.259999990463257, -0.25, -0.239999994635582, -0.230000004172325, -0.219999998807907, -0.209999993443489, -0.200000002980232, -0.189999997615814, -0.180000007152557, -0.170000001788139, -0.159999996423721, -0.150000005960464, -0.140000000596046, -0.129999995231628, -0.119999997317791, -0.109999999403954, -0.100000001490116, -0.0900000035762787, -0.0799999982118607, -0.0700000002980232, -0.0599999986588955, -0.0500000007450581, -0.0399999991059303, -0.0299999993294477, -0.0199999995529652, -0.00999999977648258, 0, 0.00999999977648258, 0.0199999995529652, 0.0299999993294477, 0.0399999991059303, 0.0500000007450581, 0.0599999986588955, 0.0700000002980232, 0.0799999982118607, 0.0900000035762787, 0.100000001490116, 0.109999999403954, 0.119999997317791, 0.129999995231628, 0.140000000596046, 0.150000005960464, 0.159999996423721, 0.170000001788139, 0.180000007152557, 0.189999997615814, 0.200000002980232, 0.209999993443489, 0.219999998807907, 0.230000004172325, 0.239999994635582, 0.25, 0.259999990463257, 0.270000010728836, 0.280000001192093, 0.28999999165535, 0.300000011920929, 0.310000002384186, 0.319999992847443, 0.330000013113022, 0.340000003576279, 0.349999994039536, 0.360000014305115, 0.370000004768372, 0.379999995231628, 0.389999985694885, 0.400000005960464, 0.409999996423721, 0.419999986886978, 0.430000007152557, 0.439999997615814, 0.449999988079071, 0.46000000834465, 0.469999998807907, 0.479999989271164, 0.490000009536743, 0.5, 0.509999990463257, 0.519999980926514, 0.529999971389771, 0.540000021457672, 0.550000011920928, 0.560000002384186, 0.569999992847443, 0.579999983310699, 0.589999973773956, 0.600000023841858, 0.610000014305115, 0.620000004768372, 0.629999995231628, 0.639999985694885, 0.649999976158142, 0.660000026226044, 0.670000016689301, 0.680000007152557, 0.689999997615814, 0.699999988079071, 0.709999978542328, 0.720000028610229, 0.730000019073486, 0.740000009536743, 0.75, 0.759999990463257, 0.769999980926514, 0.779999971389771, 0.790000021457672, 0.800000011920928, 0.810000002384186, 0.819999992847443, 0.829999983310699, 0.839999973773956, 0.850000023841858, 0.860000014305115, 0.870000004768372, 0.879999995231628, 0.889999985694885, 0.899999976158142, 0.910000026226044, 0.920000016689301, 0.930000007152557, 0.939999997615814, 0.949999988079071, 0.959999978542328, 0.970000028610229, 0.980000019073486, 0.990000009536743, 1, 1, 0.990000009536743, 0.980000019073486, 0.970000028610229, 0.959999978542328, 0.949999988079071, 0.939999997615814, 0.930000007152557, 0.920000016689301, 0.910000026226044, 0.899999976158142, 0.889999985694885, 0.879999995231628, 0.870000004768372, 0.860000014305115, 0.850000023841858, 0.839999973773956, 0.829999983310699, 0.819999992847443, 0.810000002384186, 0.800000011920928, 0.790000021457672, 0.779999971389771, 0.769999980926514, 0.759999990463257, 0.75, 0.740000009536743, 0.730000019073486, 0.720000028610229, 0.709999978542328, 0.699999988079071, 0.689999997615814, 0.680000007152557, 0.670000016689301, 0.660000026226044, 0.649999976158142, 0.639999985694885, 0.629999995231628, 0.620000004768372, 0.610000014305115, 0.600000023841858, 0.589999973773956, 0.579999983310699, 0.569999992847443, 0.560000002384186, 0.550000011920928, 0.540000021457672, 0.529999971389771, 0.519999980926514, 0.509999990463257, 0.5, 0.490000009536743, 0.479999989271164, 0.469999998807907, 0.46000000834465, 0.449999988079071, 0.439999997615814, 0.430000007152557, 0.419999986886978, 0.409999996423721, 0.400000005960464, 0.389999985694885, 0.379999995231628, 0.370000004768372, 0.360000014305115, 0.349999994039536, 0.340000003576279, 0.330000013113022, 0.319999992847443, 0.310000002384186, 0.300000011920929, 0.28999999165535, 0.280000001192093, 0.270000010728836, 0.259999990463257, 0.25, 0.239999994635582, 0.230000004172325, 0.219999998807907, 0.209999993443489, 0.200000002980232, 0.189999997615814, 0.180000007152557, 0.170000001788139, 0.159999996423721, 0.150000005960464, 0.140000000596046, 0.129999995231628, 0.119999997317791, 0.109999999403954, 0.100000001490116, 0.0900000035762787, 0.0799999982118607, 0.0700000002980232, 0.0599999986588955, 0.0500000007450581, 0.0399999991059303, 0.0299999993294477, 0.0199999995529652, 0.00999999977648258, 0, -0.00999999977648258, -0.0199999995529652, -0.0299999993294477, -0.0399999991059303, -0.0500000007450581, -0.0599999986588955, -0.0700000002980232, -0.0799999982118607, -0.0900000035762787, -0.100000001490116, -0.109999999403954, -0.119999997317791, -0.129999995231628, -0.140000000596046, -0.150000005960464, -0.159999996423721, -0.170000001788139, -0.180000007152557, -0.189999997615814, -0.200000002980232, -0.209999993443489, -0.219999998807907, -0.230000004172325, -0.239999994635582, -0.25, -0.259999990463257, -0.270000010728836, -0.280000001192093, -0.28999999165535, -0.300000011920929, -0.310000002384186, -0.319999992847443, -0.330000013113022, -0.340000003576279, -0.349999994039536, -0.360000014305115, -0.370000004768372, -0.379999995231628, -0.389999985694885, -0.400000005960464, -0.409999996423721, -0.419999986886978, -0.430000007152557, -0.439999997615814, -0.449999988079071, -0.46000000834465, -0.469999998807907, -0.479999989271164, -0.490000009536743, -0.5, -0.509999990463257, -0.519999980926514, -0.529999971389771, -0.540000021457672, -0.550000011920928, -0.560000002384186, -0.569999992847443, -0.579999983310699, -0.589999973773956, -0.600000023841858, -0.610000014305115, -0.620000004768372, -0.629999995231628, -0.639999985694885, -0.649999976158142, -0.660000026226044, -0.670000016689301, -0.680000007152557, -0.689999997615814, -0.699999988079071, -0.709999978542328, -0.720000028610229, -0.730000019073486, -0.740000009536743, -0.75, -0.759999990463257, -0.769999980926514, -0.779999971389771, -0.790000021457672, -0.800000011920928, -0.810000002384186, -0.819999992847443, -0.829999983310699, -0.839999973773956, -0.850000023841858, -0.860000014305115, -0.870000004768372, -0.879999995231628, -0.889999985694885, -0.899999976158142, -0.910000026226044, -0.920000016689301, -0.930000007152557, -0.939999997615814, -0.949999988079071, -0.959999978542328, -0.970000028610229, -0.980000019073486, -0.990000009536743, -1]

cell_gel_i = [-3.98927E-05, -3.8197E-05, -3.711E-05, -3.62255E-05, -3.53798E-05, -3.47115E-05, -3.40843E-05, -3.34248E-05, -3.27669E-05, -3.21529E-05, -3.15528E-05, -3.0943E-05, -3.03753E-05, -2.98489E-05, -2.92692E-05, -2.87332E-05, -2.81973E-05, -2.76738E-05, -2.71395E-05, -2.66414E-05, -2.61069E-05, -2.561E-05, -2.51333E-05, -2.46504E-05, -2.41459E-05, -2.36557E-05, -2.31594E-05, -2.26529E-05, -2.21911E-05, -2.17342E-05, -2.12891E-05, -2.08648E-05, -2.04414E-05, -2.00144E-05, -1.96166E-05, -1.92128E-05, -1.88165E-05, -1.84404E-05, -1.80716E-05, -1.77054E-05, -1.73413E-05, -1.69926E-05, -1.66193E-05, -1.62626E-05, -1.59154E-05, -1.55732E-05, -1.52439E-05, -1.4907E-05, -1.45718E-05, -1.42425E-05, -1.39142E-05, -1.35961E-05, -1.32815E-05, -1.29556E-05, -1.2632E-05, -1.23124E-05, -1.19935E-05, -1.16686E-05, -1.13448E-05, -1.10027E-05, -1.06686E-05, -1.03416E-05, -1.00055E-05, -9.56674E-06, -9.2509E-06, -8.91802E-06, -8.58028E-06, -8.23928E-06, -7.88713E-06, -7.53513E-06, -7.17758E-06, -6.8148E-06, -6.44303E-06, -6.06469E-06, -5.67791E-06, -5.28119E-06, -4.88329E-06, -4.4915E-06, -4.09948E-06, -3.71974E-06, -3.35676E-06, -3.01471E-06, -2.69501E-06, -2.40201E-06, -2.13564E-06, -1.89096E-06, -1.66984E-06, -1.46929E-06, -1.29029E-06, -1.13187E-06, -9.95287E-07, -8.65814E-07, -7.43823E-07, -6.35074E-07, -5.35246E-07, -4.45426E-07, -3.64203E-07, -2.905E-07, -2.27097E-07, -1.66639E-07, -1.13993E-07, -6.63869E-08, -2.39295E-08, 1.17388E-08, 4.58264E-08, 7.62762E-08, 1.02634E-07, 1.27584E-07, 1.49403E-07, 1.69519E-07, 1.89303E-07, 2.0716E-07, 2.23222E-07, 2.41365E-07, 2.57541E-07, 2.73887E-07, 2.89637E-07, 3.04866E-07, 3.22376E-07, 3.37445E-07, 3.55079E-07, 3.71301E-07, 3.8911E-07, 4.06492E-07, 4.26828E-07, 4.48668E-07, 4.72365E-07, 5.00189E-07, 5.33164E-07, 5.73851E-07, 6.24015E-07, 6.87279E-07, 7.66047E-07, 8.66806E-07, 9.85064E-07, 1.00855E-06, 1.17881E-06, 1.36565E-06, 1.57011E-06, 1.78348E-06, 2.00174E-06, 2.22087E-06, 2.43387E-06, 2.64129E-06, 2.83157E-06, 3.00636E-06, 3.1664E-06, 3.30353E-06, 3.42141E-06, 3.52328E-06, 3.60924E-06, 3.68254E-06, 3.7449E-06, 3.79614E-06, 3.84259E-06, 3.88349E-06, 3.92065E-06, 3.95408E-06, 3.98543E-06, 4.01819E-06, 4.04947E-06, 4.07709E-06, 4.10721E-06, 4.13992E-06, 4.17464E-06, 4.21234E-06, 4.2495E-06, 4.28364E-06, 4.32494E-06, 4.36285E-06, 4.41483E-06, 4.46715E-06, 4.51869E-06, 4.57917E-06, 4.64432E-06, 4.71056E-06, 4.78601E-06, 4.86082E-06, 4.94557E-06, 5.0357E-06, 5.13648E-06, 5.24673E-06, 5.3719E-06, 5.50746E-06, 5.65481E-06, 5.81042E-06, 5.98889E-06, 6.18428E-06, 6.43321E-06, 6.70641E-06, 7.0236E-06, 7.37105E-06, 7.762E-06, 8.15961E-06, 8.55303E-06, 8.91736E-06, 9.25678E-06, 9.56393E-06, 9.84293E-06, 1.01151E-05, 9.45171E-06, 1.76554E-05, 1.30725E-05, 1.06465E-05, 8.43714E-06, 7.32681E-06, 6.4504E-06, 5.72731E-06, 5.11153E-06, 4.57857E-06, 4.1167E-06, 3.70206E-06, 3.33754E-06, 3.0182E-06, 2.72233E-06, 2.46201E-06, 2.22438E-06, 2.0112E-06, 1.81761E-06, 1.63901E-06, 1.47694E-06, 1.32387E-06, 1.18012E-06, 1.03965E-06, 1.28706E-06, 1.07051E-06, 1.21543E-06, 1.08373E-06, 1.00865E-06, 1.04649E-06, 9.64993E-07, 9.13786E-07, 8.79031E-07, 8.47004E-07, 8.22424E-07, 7.9671E-07, 7.72825E-07, 7.52702E-07, 7.29094E-07, 7.10056E-07, 6.93315E-07, 6.75331E-07, 6.59033E-07, 6.44888E-07, 6.29445E-07, 6.14354E-07, 6.01768E-07, 5.85083E-07, 5.71033E-07, 5.53316E-07, 5.36864E-07, 5.20435E-07, 4.9883E-07, 4.78905E-07, 4.54014E-07, 4.28814E-07, 4.00848E-07, 3.70358E-07, 3.3864E-07, 3.02753E-07, 2.72903E-07, 2.28768E-07, 1.90389E-07, 1.56515E-07, 1.19977E-07, 8.3309E-08, 5.56137E-08, 2.82809E-08, 4.65855E-09, -8.6401E-09, -1.99875E-08, -3.05312E-08, -3.7629E-08, -4.22131E-08, -4.50473E-08, -4.61232E-08, -4.80316E-08, -4.89193E-08, -5.14082E-08, -5.01777E-08, -5.21513E-08, -5.2191E-08, -5.46156E-08, -5.61432E-08, -5.86997E-08, -5.85702E-08, -6.23775E-08, -6.4956E-08, -6.80611E-08, -7.24376E-08, -7.70754E-08, -8.00752E-08, -8.37112E-08, -9.0449E-08, -9.82003E-08, -1.0365E-07, -1.12495E-07, -1.22338E-07, -1.32997E-07, -1.45713E-07, -1.60741E-07, -1.76468E-07, -1.94712E-07, -2.16163E-07, -2.40799E-07, -2.68524E-07, -2.99978E-07, -3.356E-07, -3.72764E-07, -4.16781E-07, -4.66459E-07, -5.20605E-07, -5.79602E-07, -6.44033E-07, -7.16328E-07, -7.92953E-07, -8.75486E-07, -9.65401E-07, -1.0473E-06, -1.14825E-06, -1.2546E-06, -1.36616E-06, -1.48156E-06, -1.60264E-06, -1.72921E-06, -1.85958E-06, -1.99438E-06, -2.1376E-06, -2.28193E-06, -2.43341E-06, -2.58737E-06, -2.74627E-06, -2.91348E-06, -3.08408E-06, -3.26122E-06, -3.44882E-06, -3.64162E-06, -3.84617E-06, -4.06241E-06, -4.29276E-06, -4.54206E-06, -4.80112E-06, -5.06764E-06, -5.35236E-06, -5.64981E-06, -5.95447E-06, -6.26618E-06, -6.59442E-06, -6.93002E-06, -7.27536E-06, -7.61642E-06, -7.96397E-06, -8.3237E-06, -8.68425E-06, -9.04277E-06, -9.39326E-06, -9.73103E-06, -1.0075E-05, -1.04072E-05, -1.06956E-05, -1.10417E-05, -1.13977E-05, -1.17561E-05, -1.21132E-05, -1.24623E-05, -1.28151E-05, -1.31809E-05, -1.35354E-05, -1.39232E-05, -1.42252E-05, -1.45686E-05, -1.49095E-05, -1.5255E-05, -1.55923E-05, -1.59274E-05, -1.62612E-05, -1.65906E-05, -1.69261E-05, -1.72639E-05, -1.75867E-05, -1.79115E-05, -1.82371E-05, -1.8564E-05, -1.88901E-05, -1.92067E-05, -1.9509E-05, -1.98535E-05, -2.01934E-05, -2.05183E-05, -2.08372E-05, -2.11583E-05, -2.14616E-05, -2.1782E-05, -2.21204E-05, -2.24672E-05, -2.28065E-05, -2.31767E-05, -2.36016E-05, -2.40815E-05, -2.45862E-05, -2.5127E-05, -2.57215E-05]

cell_no_gel = [-1.75826E-05, -2.33471E-05, -2.62414E-05, -2.88422E-05, -3.01731E-05, -3.12368E-05, -3.15588E-05, -3.14834E-05, -3.1125E-05, -3.05662E-05, -3.00718E-05, -2.94225E-05, -2.88436E-05, -2.83455E-05, -2.77613E-05, -2.72833E-05, -2.68137E-05, -2.63225E-05, -2.58131E-05, -2.52898E-05, -2.48187E-05, -2.4363E-05, -2.39056E-05, -2.34756E-05, -2.30466E-05, -2.26364E-05, -2.21913E-05, -2.17251E-05, -2.12495E-05, -2.07864E-05, -2.03414E-05, -1.99101E-05, -1.94375E-05, -1.88971E-05, -1.85851E-05, -1.81641E-05, -1.77915E-05, -1.73962E-05, -1.69842E-05, -1.65735E-05, -1.61507E-05, -1.57617E-05, -1.5367E-05, -1.49625E-05, -1.45905E-05, -1.42179E-05, -1.38412E-05, -1.34604E-05, -1.30931E-05, -1.27626E-05, -1.24193E-05, -1.2086E-05, -1.17494E-05, -1.14273E-05, -1.1099E-05, -1.07646E-05, -1.03715E-05, -1.00182E-05, -9.59631E-06, -9.2433E-06, -8.86899E-06, -8.48788E-06, -8.13215E-06, -7.76589E-06, -7.33288E-06, -6.95924E-06, -6.58212E-06, -6.19943E-06, -5.78603E-06, -5.40523E-06, -5.02316E-06, -4.64453E-06, -4.27754E-06, -3.9197E-06, -3.58126E-06, -3.25483E-06, -2.95466E-06, -2.67678E-06, -2.41908E-06, -2.18421E-06, -1.97318E-06, -1.77388E-06, -1.6062E-06, -1.43972E-06, -1.29376E-06, -1.15867E-06, -1.04079E-06, -9.31814E-07, -8.22841E-07, -7.27464E-07, -6.4078E-07, -5.57918E-07, -4.81796E-07, -4.09483E-07, -3.46469E-07, -2.88708E-07, -2.33417E-07, -1.84733E-07, -1.3287E-07, -1.01754E-07, -6.35968E-08, -3.95458E-08, -5.32816E-09, 1.96249E-08, 3.56193E-08, 6.2844E-08, 8.46752E-08, 9.00183E-08, 1.11689E-07, 1.27949E-07, 1.39374E-07, 1.53882E-07, 1.63578E-07, 1.74793E-07, 1.80213E-07, 1.96831E-07, 2.07811E-07, 2.18729E-07, 2.29478E-07, 2.37841E-07, 2.50474E-07, 2.63801E-07, 2.78207E-07, 2.87243E-07, 3.02592E-07, 3.16786E-07, 3.34366E-07, 3.64363E-07, 3.94852E-07, 4.31927E-07, 4.84557E-07, 5.3415E-07, 6.16655E-07, 7.00322E-07, 7.9802E-07, 9.00438E-07, 1.01689E-06, 1.03333E-06, 1.15613E-06, 1.27961E-06, 1.39316E-06, 1.50312E-06, 1.60209E-06, 1.69228E-06, 1.77747E-06, 1.85809E-06, 1.92103E-06, 1.97007E-06, 2.02935E-06, 2.07281E-06, 2.11594E-06, 2.15755E-06, 2.19242E-06, 2.23001E-06, 2.26652E-06, 2.30069E-06, 2.33653E-06, 2.3671E-06, 2.39506E-06, 2.43573E-06, 2.47035E-06, 2.49785E-06, 2.54795E-06, 2.57239E-06, 2.60235E-06, 2.6466E-06, 2.68512E-06, 2.72639E-06, 2.77362E-06, 2.8075E-06, 2.85615E-06, 2.91008E-06, 2.95888E-06, 3.01575E-06, 3.07869E-06, 3.14411E-06, 3.23257E-06, 3.3089E-06, 3.4118E-06, 3.51212E-06, 3.63263E-06, 3.74231E-06, 3.87328E-06, 4.03118E-06, 4.19336E-06, 4.42368E-06, 4.70413E-06, 4.99506E-06, 5.28346E-06, 5.52169E-06, 5.70173E-06, 5.87533E-06, 6.03607E-06, 6.17752E-06, 6.33053E-06, 6.51609E-06, 6.74746E-06, 7.00228E-06, 7.29819E-06, 7.69072E-06, 8.1523E-06, 1.62595E-05, 1.07851E-05, 7.41951E-06, 6.20996E-06, 5.30273E-06, 4.60617E-06, 4.04863E-06, 3.58473E-06, 3.18865E-06, 2.873E-06, 2.59443E-06, 2.34555E-06, 2.11811E-06, 1.9203E-06, 1.7125E-06, 1.52053E-06, 1.33713E-06, 1.17337E-06, 1.0322E-06, 1.24245E-06, 1.02184E-06, 1.01775E-06, 8.53172E-07, 7.42133E-07, 6.56369E-07, 6.01307E-07, 5.69201E-07, 5.60987E-07, 5.84669E-07, 6.23647E-07, 6.54154E-07, 6.76643E-07, 6.83795E-07, 6.91548E-07, 6.90478E-07, 6.91504E-07, 6.87296E-07, 6.83268E-07, 6.76971E-07, 6.68126E-07, 6.67697E-07, 6.57842E-07, 6.47063E-07, 6.35946E-07, 6.22007E-07, 6.22314E-07, 6.09496E-07, 5.9952E-07, 5.81705E-07, 5.66749E-07, 5.54036E-07, 5.41142E-07, 5.1973E-07, 5.06061E-07, 4.89666E-07, 4.69923E-07, 4.60164E-07, 4.25254E-07, 4.00466E-07, 3.7271E-07, 3.3446E-07, 2.99004E-07, 2.67429E-07, 2.21551E-07, 1.77258E-07, 1.36114E-07, 9.3365E-08, 6.155E-08, 3.49655E-08, 1.28185E-08, -9.09911E-09, -2.53725E-08, -3.54158E-08, -4.29303E-08, -4.86047E-08, -5.13053E-08, -7.32263E-08, -5.49078E-08, -5.62113E-08, -6.14292E-08, -7.56762E-08, -7.44884E-08, -6.99602E-08, -7.83129E-08, -7.11002E-08, -8.84671E-08, -8.87985E-08, -9.16438E-08, -9.916E-08, -1.1064E-07, -1.11364E-07, -1.20483E-07, -1.29277E-07, -1.36139E-07, -1.55271E-07, -1.59958E-07, -1.70724E-07, -1.87947E-07, -2.10431E-07, -2.21544E-07, -2.31689E-07, -2.74416E-07, -2.9296E-07, -3.20129E-07, -3.51345E-07, -3.89922E-07, -4.2713E-07, -4.68824E-07, -5.1272E-07, -5.65376E-07, -6.2993E-07, -6.89704E-07, -7.63172E-07, -8.42584E-07, -9.1187E-07, -9.99664E-07, -1.08346E-06, -1.17912E-06, -1.28714E-06, -1.40353E-06, -1.51885E-06, -1.64319E-06, -1.77171E-06, -1.90026E-06, -2.04163E-06, -2.18128E-06, -2.33065E-06, -2.48521E-06, -2.64001E-06, -2.80657E-06, -2.97839E-06, -3.15773E-06, -3.34875E-06, -3.55387E-06, -3.78462E-06, -4.03406E-06, -4.31426E-06, -4.62561E-06, -4.96404E-06, -5.3243E-06, -5.72717E-06, -6.14133E-06, -6.56289E-06, -7.01017E-06, -7.46639E-06, -7.92381E-06, -8.38493E-06, -8.84638E-06, -9.30918E-06, -9.76704E-06, -1.02287E-05, -1.06871E-05, -1.11314E-05, -1.15793E-05, -1.2025E-05, -1.24629E-05, -1.29157E-05, -1.33653E-05, -1.38078E-05, -1.42561E-05, -1.47039E-05, -1.51461E-05, -1.55907E-05, -1.60317E-05, -1.64681E-05, -1.69119E-05, -1.73546E-05, -1.77879E-05, -1.82195E-05, -1.86519E-05, -1.90768E-05, -1.95032E-05, -1.99243E-05, -2.03459E-05, -2.0761E-05, -2.11787E-05, -2.15918E-05, -2.19976E-05, -2.23999E-05, -2.27992E-05, -2.32018E-05, -2.36123E-05, -2.40031E-05, -2.43998E-05, -2.47907E-05, -2.51672E-05, -2.55417E-05, -2.59195E-05, -2.629E-05, -2.66539E-05, -2.70113E-05, -2.73644E-05, -2.77235E-05, -2.80768E-05, -2.84196E-05, -2.87663E-05, -2.91188E-05, -2.95138E-05, -2.99117E-05, -3.03597E-05, -3.07616E-05]

plt.figure(num = 1, figsize=(10,6), dpi= 300)
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
