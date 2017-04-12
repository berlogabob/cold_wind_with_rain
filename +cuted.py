# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cell_v = [-1, -0.990000009536743, -0.980000019073486, -0.970000028610229, -0.959999978542328, -0.949999988079071, -0.939999997615814, -0.930000007152557, -0.920000016689301, -0.910000026226044, -0.899999976158142, -0.889999985694885, -0.879999995231628, -0.870000004768372, -0.860000014305115, -0.850000023841858, -0.839999973773956, -0.829999983310699, -0.819999992847443, -0.810000002384186, -0.800000011920928, -0.790000021457672, -0.779999971389771, -0.769999980926514, -0.759999990463257, -0.75, -0.740000009536743, -0.730000019073486, -0.720000028610229, -0.709999978542328, -0.699999988079071, -0.689999997615814, -0.680000007152557, -0.670000016689301, -0.660000026226044, -0.649999976158142, -0.639999985694885, -0.629999995231628, -0.620000004768372, -0.610000014305115, -0.600000023841858, -0.589999973773956, -0.579999983310699, -0.569999992847443, -0.560000002384186, -0.550000011920928, -0.540000021457672, -0.529999971389771, -0.519999980926514, -0.509999990463257, -0.5, -0.490000009536743, -0.479999989271164, -0.469999998807907, -0.46000000834465, -0.449999988079071, -0.439999997615814, -0.430000007152557, -0.419999986886978, -0.409999996423721, -0.400000005960464, -0.389999985694885, -0.379999995231628, -0.370000004768372, -0.360000014305115, -0.349999994039536, -0.340000003576279, -0.330000013113022, -0.319999992847443, -0.310000002384186, -0.300000011920929, -0.28999999165535, -0.280000001192093, -0.270000010728836, -0.259999990463257, -0.25, -0.239999994635582, -0.230000004172325, -0.219999998807907, -0.209999993443489, -0.200000002980232, -0.189999997615814, -0.180000007152557, -0.170000001788139, -0.159999996423721, -0.150000005960464, -0.140000000596046, -0.129999995231628, -0.119999997317791, -0.109999999403954, -0.100000001490116, -0.0900000035762787, -0.0799999982118607, -0.0700000002980232, -0.0599999986588955, -0.0500000007450581, -0.0399999991059303, -0.0299999993294477, -0.0199999995529652, -0.00999999977648258, 0, 0.00999999977648258, 0.0199999995529652, 0.0299999993294477, 0.0399999991059303, 0.0500000007450581, 0.0599999986588955, 0.0700000002980232, 0.0799999982118607, 0.0900000035762787, 0.100000001490116, 0.109999999403954, 0.119999997317791, 0.129999995231628, 0.140000000596046, 0.150000005960464, 0.159999996423721, 0.170000001788139, 0.180000007152557, 0.189999997615814, 0.200000002980232, 0.209999993443489, 0.219999998807907, 0.230000004172325, 0.239999994635582, 0.25, 0.259999990463257, 0.270000010728836, 0.280000001192093, 0.28999999165535, 0.300000011920929, 0.310000002384186, 0.319999992847443, 0.330000013113022, 0.340000003576279, 0.349999994039536, 0.360000014305115, 0.370000004768372, 0.379999995231628, 0.389999985694885, 0.400000005960464, 0.409999996423721, 0.419999986886978, 0.430000007152557, 0.439999997615814, 0.449999988079071, 0.46000000834465, 0.469999998807907, 0.479999989271164, 0.490000009536743, 0.5, 0.509999990463257, 0.519999980926514, 0.529999971389771, 0.540000021457672, 0.550000011920928, 0.560000002384186, 0.569999992847443, 0.579999983310699, 0.589999973773956, 0.600000023841858, 0.610000014305115, 0.620000004768372, 0.629999995231628, 0.639999985694885, 0.649999976158142, 0.660000026226044, 0.670000016689301, 0.680000007152557, 0.689999997615814, 0.699999988079071, 0.709999978542328, 0.720000028610229, 0.730000019073486, 0.740000009536743, 0.75, 0.759999990463257, 0.769999980926514, 0.779999971389771, 0.790000021457672, 0.800000011920928, 0.810000002384186, 0.819999992847443, 0.829999983310699, 0.839999973773956, 0.850000023841858, 0.860000014305115, 0.870000004768372, 0.879999995231628, 0.889999985694885, 0.899999976158142, 0.910000026226044, 0.920000016689301, 0.930000007152557, 0.939999997615814, 0.949999988079071, 0.959999978542328, 0.970000028610229, 0.980000019073486, 0.990000009536743, 1, 1, 0.990000009536743, 0.980000019073486, 0.970000028610229, 0.959999978542328, 0.949999988079071, 0.939999997615814, 0.930000007152557, 0.920000016689301, 0.910000026226044, 0.899999976158142, 0.889999985694885, 0.879999995231628, 0.870000004768372, 0.860000014305115, 0.850000023841858, 0.839999973773956, 0.829999983310699, 0.819999992847443, 0.810000002384186, 0.800000011920928, 0.790000021457672, 0.779999971389771, 0.769999980926514, 0.759999990463257, 0.75, 0.740000009536743, 0.730000019073486, 0.720000028610229, 0.709999978542328, 0.699999988079071, 0.689999997615814, 0.680000007152557, 0.670000016689301, 0.660000026226044, 0.649999976158142, 0.639999985694885, 0.629999995231628, 0.620000004768372, 0.610000014305115, 0.600000023841858, 0.589999973773956, 0.579999983310699, 0.569999992847443, 0.560000002384186, 0.550000011920928, 0.540000021457672, 0.529999971389771, 0.519999980926514, 0.509999990463257, 0.5, 0.490000009536743, 0.479999989271164, 0.469999998807907, 0.46000000834465, 0.449999988079071, 0.439999997615814, 0.430000007152557, 0.419999986886978, 0.409999996423721, 0.400000005960464, 0.389999985694885, 0.379999995231628, 0.370000004768372, 0.360000014305115, 0.349999994039536, 0.340000003576279, 0.330000013113022, 0.319999992847443, 0.310000002384186, 0.300000011920929, 0.28999999165535, 0.280000001192093, 0.270000010728836, 0.259999990463257, 0.25, 0.239999994635582, 0.230000004172325, 0.219999998807907, 0.209999993443489, 0.200000002980232, 0.189999997615814, 0.180000007152557, 0.170000001788139, 0.159999996423721, 0.150000005960464, 0.140000000596046, 0.129999995231628, 0.119999997317791, 0.109999999403954, 0.100000001490116, 0.0900000035762787, 0.0799999982118607, 0.0700000002980232, 0.0599999986588955, 0.0500000007450581, 0.0399999991059303, 0.0299999993294477, 0.0199999995529652, 0.00999999977648258, 0, -0.00999999977648258, -0.0199999995529652, -0.0299999993294477, -0.0399999991059303, -0.0500000007450581, -0.0599999986588955, -0.0700000002980232, -0.0799999982118607, -0.0900000035762787, -0.100000001490116, -0.109999999403954, -0.119999997317791, -0.129999995231628, -0.140000000596046, -0.150000005960464, -0.159999996423721, -0.170000001788139, -0.180000007152557, -0.189999997615814, -0.200000002980232, -0.209999993443489, -0.219999998807907, -0.230000004172325, -0.239999994635582, -0.25, -0.259999990463257, -0.270000010728836, -0.280000001192093, -0.28999999165535, -0.300000011920929, -0.310000002384186, -0.319999992847443, -0.330000013113022, -0.340000003576279, -0.349999994039536, -0.360000014305115, -0.370000004768372, -0.379999995231628, -0.389999985694885, -0.400000005960464, -0.409999996423721, -0.419999986886978, -0.430000007152557, -0.439999997615814, -0.449999988079071, -0.46000000834465, -0.469999998807907, -0.479999989271164, -0.490000009536743, -0.5, -0.509999990463257, -0.519999980926514, -0.529999971389771, -0.540000021457672, -0.550000011920928, -0.560000002384186, -0.569999992847443, -0.579999983310699, -0.589999973773956, -0.600000023841858, -0.610000014305115, -0.620000004768372, -0.629999995231628, -0.639999985694885, -0.649999976158142, -0.660000026226044, -0.670000016689301, -0.680000007152557, -0.689999997615814, -0.699999988079071, -0.709999978542328, -0.720000028610229, -0.730000019073486, -0.740000009536743, -0.75, -0.759999990463257, -0.769999980926514, -0.779999971389771, -0.790000021457672, -0.800000011920928, -0.810000002384186, -0.819999992847443, -0.829999983310699, -0.839999973773956, -0.850000023841858, -0.860000014305115, -0.870000004768372, -0.879999995231628, -0.889999985694885, -0.899999976158142, -0.910000026226044, -0.920000016689301, -0.930000007152557, -0.939999997615814, -0.949999988079071, -0.959999978542328, -0.970000028610229, -0.980000019073486, -0.990000009536743, -1]

cell_gel_i = [-4.08701E-05, -3.93842E-05, -3.81237E-05, -3.70252E-05, -3.60368E-05, -3.51105E-05, -3.42113E-05, -3.33782E-05, -3.25881E-05, -3.1745E-05, -3.09891E-05, -3.02151E-05, -2.95166E-05, -2.87909E-05, -2.8173E-05, -2.74467E-05, -2.67674E-05, -2.6066E-05, -2.54004E-05, -2.47466E-05, -2.41526E-05, -2.35418E-05, -2.2924E-05, -2.23209E-05, -2.17301E-05, -2.11707E-05, -2.05964E-05, -2.00463E-05, -1.95108E-05, -1.90045E-05, -1.85181E-05, -1.80412E-05, -1.75713E-05, -1.71345E-05, -1.66981E-05, -1.62748E-05, -1.58523E-05, -1.54777E-05, -1.5098E-05, -1.47306E-05, -1.43764E-05, -1.40326E-05, -1.37015E-05, -1.33706E-05, -1.30772E-05, -1.279E-05, -1.25147E-05, -1.22449E-05, -1.19924E-05, -1.17429E-05, -1.1502E-05, -1.12681E-05, -1.10458E-05, -1.08257E-05, -1.06115E-05, -1.04069E-05, -1.02043E-05, -1.00112E-05, -9.79938E-06, -9.62176E-06, -9.44047E-06, -9.26341E-06, -9.08336E-06, -8.8973E-06, -8.70738E-06, -8.51467E-06, -8.31409E-06, -8.10904E-06, -7.89996E-06, -7.68807E-06, -7.46859E-06, -7.25381E-06, -7.03124E-06, -6.80663E-06, -6.58345E-06, -6.35856E-06, -6.13182E-06, -5.90502E-06, -5.67838E-06, -5.45202E-06, -5.22683E-06, -5.00339E-06, -4.78039E-06, -4.55901E-06, -4.34136E-06, -4.1274E-06, -3.9144E-06, -3.70347E-06, -3.49676E-06, -3.29367E-06, -3.09687E-06, -2.90006E-06, -2.704E-06, -2.51787E-06, -2.34156E-06, -2.1665E-06, -1.99733E-06, -1.83435E-06, -1.67776E-06, -1.52724E-06, -1.38533E-06, -1.24812E-06, -1.12176E-06, -1.00206E-06, -8.82027E-07, -7.75262E-07, -6.77823E-07, -5.87173E-07, -4.98979E-07, -4.21769E-07, -3.49421E-07, -2.84665E-07, -2.2524E-07, -1.72009E-07, -1.2247E-07, -8.10688E-08, -4.35037E-08, -1.08808E-08, 1.81186E-08, 4.03916E-08, 6.19966E-08, 7.94538E-08, 9.58662E-08, 1.09073E-07, 1.20257E-07, 1.30574E-07, 1.38487E-07, 1.45892E-07, 1.53549E-07, 1.6035E-07, 1.65908E-07, 1.73159E-07, 1.78784E-07, 1.83666E-07, 1.91274E-07, 1.95784E-07, 1.9989E-07, 2.06075E-07, 2.11458E-07, 2.16832E-07, 2.23129E-07, 2.29777E-07, 2.38316E-07, 2.47409E-07, 2.5678E-07, 2.78434E-07, 2.97879E-07, 3.26938E-07, 3.64924E-07, 4.1474E-07, 4.72828E-07, 5.45238E-07, 6.28033E-07, 7.24307E-07, 8.27097E-07, 9.38733E-07, 1.00981E-06, 1.13274E-06, 1.26132E-06, 1.38598E-06, 1.50922E-06, 1.63131E-06, 1.74377E-06, 1.85251E-06, 1.96184E-06, 2.06822E-06, 2.16551E-06, 2.25959E-06, 2.34987E-06, 2.43028E-06, 2.5043E-06, 2.56393E-06, 2.6239E-06, 2.68182E-06, 2.73354E-06, 2.77673E-06, 2.82219E-06, 2.86274E-06, 2.89586E-06, 2.93022E-06, 2.95837E-06, 2.98927E-06, 3.01652E-06, 3.043E-06, 3.06031E-06, 3.08304E-06, 3.10524E-06, 3.1233E-06, 3.13853E-06, 3.15885E-06, 3.18072E-06, 3.19743E-06, 3.21128E-06, 3.22227E-06, 3.23775E-06, 3.25441E-06, 3.27037E-06, 3.28781E-06, 3.30488E-06, 3.32299E-06, 3.33945E-06, 5.5227E-06, 4.77553E-06, 4.28992E-06, 3.93736E-06, 3.65568E-06, 3.42313E-06, 3.22962E-06, 3.05933E-06, 2.9058E-06, 2.77324E-06, 2.65825E-06, 2.5415E-06, 2.44075E-06, 2.35288E-06, 2.27299E-06, 2.19829E-06, 2.13004E-06, 2.06147E-06, 1.99791E-06, 1.93154E-06, 1.86844E-06, 1.80933E-06, 1.74647E-06, 1.69209E-06, 1.64835E-06, 1.60284E-06, 1.55278E-06, 1.5119E-06, 1.50621E-06, 1.42509E-06, 1.37405E-06, 1.3275E-06, 1.28271E-06, 1.23295E-06, 1.18002E-06, 1.12409E-06, 1.07388E-06, 1.01776E-06, 9.76175E-07, 9.13577E-07, 8.5892E-07, 8.00942E-07, 7.37531E-07, 6.81415E-07, 6.23466E-07, 5.65509E-07, 5.09117E-07, 4.55067E-07, 4.0045E-07, 3.47882E-07, 2.97389E-07, 2.47799E-07, 2.04222E-07, 1.62012E-07, 1.26191E-07, 9.68225E-08, 6.91956E-08, 4.38361E-08, 2.20218E-08, 9.53823E-09, -1.32017E-09, -1.06618E-08, -1.59312E-08, -2.13267E-08, -2.39203E-08, -2.66405E-08, -3.01076E-08, -3.21616E-08, -3.38059E-08, -3.51071E-08, -3.64399E-08, -3.94884E-08, -4.13198E-08, -4.39051E-08, -6.92342E-08, -5.26128E-08, -5.61413E-08, -6.21E-08, -6.57057E-08, -7.09137E-08, -7.69213E-08, -8.24778E-08, -9.07177E-08, -1.00214E-07, -1.10679E-07, -1.23369E-07, -1.35011E-07, -1.50727E-07, -1.68086E-07, -1.89389E-07, -2.13418E-07, -2.41388E-07, -2.69099E-07, -3.02921E-07, -3.45594E-07, -3.85954E-07, -4.29728E-07, -4.74669E-07, -5.19241E-07, -5.66081E-07, -6.18221E-07, -6.84731E-07, -7.33883E-07, -8.04648E-07, -8.66347E-07, -9.33338E-07, -9.99884E-07, -1.04226E-06, -1.10997E-06, -1.17437E-06, -1.23792E-06, -1.30891E-06, -1.3718E-06, -1.426E-06, -1.48754E-06, -1.5443E-06, -1.60919E-06, -1.66084E-06, -1.70884E-06, -1.76965E-06, -1.8281E-06, -1.88909E-06, -1.93681E-06, -2.00593E-06, -2.07316E-06, -2.11477E-06, -2.17349E-06, -2.25637E-06, -2.30941E-06, -2.36171E-06, -2.4058E-06, -2.44654E-06, -2.51437E-06, -2.63057E-06, -2.71748E-06, -2.87646E-06, -3.05048E-06, -3.15956E-06, -3.24161E-06, -3.30213E-06, -3.41428E-06, -3.50376E-06, -3.62809E-06, -3.74817E-06, -3.87991E-06, -3.94567E-06, -4.11278E-06, -4.24688E-06, -4.35891E-06, -4.49719E-06, -4.61287E-06, -4.70032E-06, -4.98155E-06, -5.22051E-06, -5.45943E-06, -5.83102E-06, -6.01946E-06, -6.29346E-06, -6.68765E-06, -6.93749E-06, -7.25357E-06, -7.50114E-06, -7.86792E-06, -8.34624E-06, -8.98888E-06, -9.43752E-06, -9.73297E-06, -9.97723E-06, -1.02627E-05, -1.07434E-05, -1.09372E-05, -1.11937E-05, -1.15923E-05, -1.19442E-05, -1.23728E-05, -1.26692E-05, -1.30449E-05, -1.33487E-05, -1.36312E-05, -1.42514E-05, -1.4728E-05, -1.5122E-05, -1.54669E-05, -1.5838E-05, -1.62726E-05, -1.66931E-05, -1.71956E-05, -1.77195E-05, -1.81901E-05, -1.86176E-05, -1.91058E-05, -1.96751E-05, -2.03534E-05, -2.09477E-05, -2.14641E-05, -2.22049E-05, -2.28383E-05, -2.35447E-05, -2.42283E-05, -2.50233E-05, -2.57399E-05]

cell_no_gel = [-1.75826E-05, -2.33471E-05, -2.62414E-05, -2.88422E-05, -3.01731E-05, -3.12368E-05, -3.15588E-05, -3.14834E-05, -3.1125E-05, -3.05662E-05, -3.00718E-05, -2.94225E-05, -2.88436E-05, -2.83455E-05, -2.77613E-05, -2.72833E-05, -2.68137E-05, -2.63225E-05, -2.58131E-05, -2.52898E-05, -2.48187E-05, -2.4363E-05, -2.39056E-05, -2.34756E-05, -2.30466E-05, -2.26364E-05, -2.21913E-05, -2.17251E-05, -2.12495E-05, -2.07864E-05, -2.03414E-05, -1.99101E-05, -1.94375E-05, -1.88971E-05, -1.85851E-05, -1.81641E-05, -1.77915E-05, -1.73962E-05, -1.69842E-05, -1.65735E-05, -1.61507E-05, -1.57617E-05, -1.5367E-05, -1.49625E-05, -1.45905E-05, -1.42179E-05, -1.38412E-05, -1.34604E-05, -1.30931E-05, -1.27626E-05, -1.24193E-05, -1.2086E-05, -1.17494E-05, -1.14273E-05, -1.1099E-05, -1.07646E-05, -1.03715E-05, -1.00182E-05, -9.59631E-06, -9.2433E-06, -8.86899E-06, -8.48788E-06, -8.13215E-06, -7.76589E-06, -7.33288E-06, -6.95924E-06, -6.58212E-06, -6.19943E-06, -5.78603E-06, -5.40523E-06, -5.02316E-06, -4.64453E-06, -4.27754E-06, -3.9197E-06, -3.58126E-06, -3.25483E-06, -2.95466E-06, -2.67678E-06, -2.41908E-06, -2.18421E-06, -1.97318E-06, -1.77388E-06, -1.6062E-06, -1.43972E-06, -1.29376E-06, -1.15867E-06, -1.04079E-06, -9.31814E-07, -8.22841E-07, -7.27464E-07, -6.4078E-07, -5.57918E-07, -4.81796E-07, -4.09483E-07, -3.46469E-07, -2.88708E-07, -2.33417E-07, -1.84733E-07, -1.3287E-07, -1.01754E-07, -6.35968E-08, -3.95458E-08, -5.32816E-09, 1.96249E-08, 3.56193E-08, 6.2844E-08, 8.46752E-08, 9.00183E-08, 1.11689E-07, 1.27949E-07, 1.39374E-07, 1.53882E-07, 1.63578E-07, 1.74793E-07, 1.80213E-07, 1.96831E-07, 2.07811E-07, 2.18729E-07, 2.29478E-07, 2.37841E-07, 2.50474E-07, 2.63801E-07, 2.78207E-07, 2.87243E-07, 3.02592E-07, 3.16786E-07, 3.34366E-07, 3.64363E-07, 3.94852E-07, 4.31927E-07, 4.84557E-07, 5.3415E-07, 6.16655E-07, 7.00322E-07, 7.9802E-07, 9.00438E-07, 1.01689E-06, 1.03333E-06, 1.15613E-06, 1.27961E-06, 1.39316E-06, 1.50312E-06, 1.60209E-06, 1.69228E-06, 1.77747E-06, 1.85809E-06, 1.92103E-06, 1.97007E-06, 2.02935E-06, 2.07281E-06, 2.11594E-06, 2.15755E-06, 2.19242E-06, 2.23001E-06, 2.26652E-06, 2.30069E-06, 2.33653E-06, 2.3671E-06, 2.39506E-06, 2.43573E-06, 2.47035E-06, 2.49785E-06, 2.54795E-06, 2.57239E-06, 2.60235E-06, 2.6466E-06, 2.68512E-06, 2.72639E-06, 2.77362E-06, 2.8075E-06, 2.85615E-06, 2.91008E-06, 2.95888E-06, 3.01575E-06, 3.07869E-06, 3.14411E-06, 3.23257E-06, 3.3089E-06, 3.4118E-06, 3.51212E-06, 3.63263E-06, 3.74231E-06, 3.87328E-06, 4.03118E-06, 4.19336E-06, 4.42368E-06, 4.70413E-06, 4.99506E-06, 5.28346E-06, 5.52169E-06, 5.70173E-06, 5.87533E-06, 6.03607E-06, 6.17752E-06, 6.33053E-06, 6.51609E-06, 6.74746E-06, 7.00228E-06, 7.29819E-06, 7.69072E-06, 8.1523E-06, 1.62595E-05, 1.07851E-05, 7.41951E-06, 6.20996E-06, 5.30273E-06, 4.60617E-06, 4.04863E-06, 3.58473E-06, 3.18865E-06, 2.873E-06, 2.59443E-06, 2.34555E-06, 2.11811E-06, 1.9203E-06, 1.7125E-06, 1.52053E-06, 1.33713E-06, 1.17337E-06, 1.0322E-06, 1.24245E-06, 1.02184E-06, 1.01775E-06, 8.53172E-07, 7.42133E-07, 6.56369E-07, 6.01307E-07, 5.69201E-07, 5.60987E-07, 5.84669E-07, 6.23647E-07, 6.54154E-07, 6.76643E-07, 6.83795E-07, 6.91548E-07, 6.90478E-07, 6.91504E-07, 6.87296E-07, 6.83268E-07, 6.76971E-07, 6.68126E-07, 6.67697E-07, 6.57842E-07, 6.47063E-07, 6.35946E-07, 6.22007E-07, 6.22314E-07, 6.09496E-07, 5.9952E-07, 5.81705E-07, 5.66749E-07, 5.54036E-07, 5.41142E-07, 5.1973E-07, 5.06061E-07, 4.89666E-07, 4.69923E-07, 4.60164E-07, 4.25254E-07, 4.00466E-07, 3.7271E-07, 3.3446E-07, 2.99004E-07, 2.67429E-07, 2.21551E-07, 1.77258E-07, 1.36114E-07, 9.3365E-08, 6.155E-08, 3.49655E-08, 1.28185E-08, -9.09911E-09, -2.53725E-08, -3.54158E-08, -4.29303E-08, -4.86047E-08, -5.13053E-08, -7.32263E-08, -5.49078E-08, -5.62113E-08, -6.14292E-08, -7.56762E-08, -7.44884E-08, -6.99602E-08, -7.83129E-08, -7.11002E-08, -8.84671E-08, -8.87985E-08, -9.16438E-08, -9.916E-08, -1.1064E-07, -1.11364E-07, -1.20483E-07, -1.29277E-07, -1.36139E-07, -1.55271E-07, -1.59958E-07, -1.70724E-07, -1.87947E-07, -2.10431E-07, -2.21544E-07, -2.31689E-07, -2.74416E-07, -2.9296E-07, -3.20129E-07, -3.51345E-07, -3.89922E-07, -4.2713E-07, -4.68824E-07, -5.1272E-07, -5.65376E-07, -6.2993E-07, -6.89704E-07, -7.63172E-07, -8.42584E-07, -9.1187E-07, -9.99664E-07, -1.08346E-06, -1.17912E-06, -1.28714E-06, -1.40353E-06, -1.51885E-06, -1.64319E-06, -1.77171E-06, -1.90026E-06, -2.04163E-06, -2.18128E-06, -2.33065E-06, -2.48521E-06, -2.64001E-06, -2.80657E-06, -2.97839E-06, -3.15773E-06, -3.34875E-06, -3.55387E-06, -3.78462E-06, -4.03406E-06, -4.31426E-06, -4.62561E-06, -4.96404E-06, -5.3243E-06, -5.72717E-06, -6.14133E-06, -6.56289E-06, -7.01017E-06, -7.46639E-06, -7.92381E-06, -8.38493E-06, -8.84638E-06, -9.30918E-06, -9.76704E-06, -1.02287E-05, -1.06871E-05, -1.11314E-05, -1.15793E-05, -1.2025E-05, -1.24629E-05, -1.29157E-05, -1.33653E-05, -1.38078E-05, -1.42561E-05, -1.47039E-05, -1.51461E-05, -1.55907E-05, -1.60317E-05, -1.64681E-05, -1.69119E-05, -1.73546E-05, -1.77879E-05, -1.82195E-05, -1.86519E-05, -1.90768E-05, -1.95032E-05, -1.99243E-05, -2.03459E-05, -2.0761E-05, -2.11787E-05, -2.15918E-05, -2.19976E-05, -2.23999E-05, -2.27992E-05, -2.32018E-05, -2.36123E-05, -2.40031E-05, -2.43998E-05, -2.47907E-05, -2.51672E-05, -2.55417E-05, -2.59195E-05, -2.629E-05, -2.66539E-05, -2.70113E-05, -2.73644E-05, -2.77235E-05, -2.80768E-05, -2.84196E-05, -2.87663E-05, -2.91188E-05, -2.95138E-05, -2.99117E-05, -3.03597E-05, -3.07616E-05]

plt.figure(num = 1, figsize=(10,6), dpi= 600)
#plt.suptitle("usinp_title", fontsize=16)
plt.plot(cell_v, cell_gel_i, "b", cell_v, cell_no_gel, "r")
#plt.plot(cell_v, cell_no_gel, "r")

plt.xlabel('millivolt')
plt.ylabel('microampere')
plt.grid(True)
#вывод
plt.figure(1).savefig("20170411" + 'e' + '.png')
plt.figure(1).savefig("20170411" + 'e' + '.pdf')
plt.show()