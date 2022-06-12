"""
Air Properties Data

Source: Cengel & Boles, ASHRAE
"""

saturation_pressure_data = [[-40,0.0019],[-35,0.0026],[-30,0.0035],[-25,0.0046],
                            [-20,0.0062],[-15,0.0082],[-10,0.0109],[-5,0.0142],
                            [0,0.0185],[5,0.024],[10,0.0309],[15,0.0369],
                            [20,0.0505],[25,0.0641],[30,0.0808],[32,0.0886],
                            [32.018,0.08866],[35,0.09992],[40,0.12166],[45,0.14748],
                            [50,0.17803],[60,0.2563],[70,0.3632],[80,0.5073],
                            [90,0.6988],[100,0.9503],[110,1.2763],[120,1.6945],
                            [130,2.225],[140,2.892],[150,3.722],[160,4.745],
                            [170,5.996],[180,7.515],[190,9.343],[200,11.529],
                            [210,14.125],[212,14.698],[220,17.188],[230,20.78],
                            [240,24.97],[250,29.82],[260,35.42],[270,41.85],
                            [280,49.18],[290,57.53],[300,66.98],[310,77.64],
                            [320,89.6],[330,103],[340,117.93],[350,134.53],
                            [360,152.92],[370,173.23],[380,195.6],[390,220.2],
                            [400,247.1],[410,276.5],[420,308.5],[430,343.3],
                            [440,381.2],[450,422.1],[460,466.3],[470,514.1],
                            [480,565.5],[490,620.7],[500,680],[520,811.4],
                            [540,961.5],[560,1131.8]]

saturation_temperature_data = [[0.000116,-80],[0.000125,-79],[0.000135,-78],[0.000145,-77],[0.000157,-76],[0.000169,-75],
                               [0.000182,-74],[0.000196,-73],[0.000211,-72],[0.000227,-71],[0.000244,-70],[0.000263,-69],
                               [0.000283,-68],[0.000304,-67],[0.000326,-66],[0.00035,-65],[0.000376,-64],[0.000404,-63],
                               [0.000433,-62],[0.000464,-61],[0.000498,-60],[0.000533,-59],[0.000571,-58],[0.000612,-57],
                               [0.000655,-56],[0.000701,-55],[0.000749,-54],[0.000801,-53],[0.000857,-52],[0.000916,-51],
                               [0.000978,-50],[0.001045,-49],[0.001115,-48],[0.001191,-47],[0.00127,-46],[0.001355,-45],
                               [0.001445,-44],[0.00154,-43],[0.001641,-42],[0.001749,-41],[0.001862,-40],[0.001983,-39],
                               [0.002111,-38],[0.002246,-37],[0.002389,-36],[0.002541,-35],[0.002701,-34],[0.002871,-33],
                               [0.003051,-32],[0.003241,-31],[0.003442,-30],[0.003654,-29],[0.003878,-28],[0.004115,-27],
                               [0.004365,-26],[0.004629,-25],[0.004908,-24],[0.005202,-23],[0.005512,-22],[0.005839,-21],
                               [0.006184,-20],[0.006548,-19],[0.006932,-18],[0.007335,-17],[0.007761,-16],[0.008209,-15],
                               [0.008681,-14],[0.009177,-13],[0.0097,-12],[0.010249,-11],[0.010827,-10],[0.011435,-9],
                               [0.012075,-8],[0.012747,-7],[0.013453,-6],[0.014194,-5],[0.014974,-4],[0.015792,-3],
                               [0.016651,-2],[0.017553,-1],[0.018499,0],[0.019492,1],[0.020533,2],[0.021625,3],
                               [0.02277,4],[0.023971,5],[0.025229,6],[0.026547,7],[0.027929,8],[0.029375,9],
                               [0.03089,10],[0.032476,11],[0.034136,12],[0.035874,13],[0.037692,14],[0.039593,15],
                               [0.041582,16],[0.043662,17],[0.045837,18],[0.048109,19],[0.050485,20],[0.052967,21],
                               [0.05556,22],[0.058268,23],[0.061096,24],[0.064048,25],[0.06713,26],[0.070347,27],
                               [0.073704,28],[0.077206,29],[0.080858,30],[0.084668,31],[0.08864,32],[0.08865,32],
                               [0.09229,33],[0.09607,34],[0.09998,35],[0.10403,36],[0.10823,37],[0.11258,38],
                               [0.11708,39],[0.12173,40],[0.12656,41],[0.13155,42],[0.13671,43],[0.14205,44],
                               [0.14757,45],[0.15328,46],[0.15919,47],[0.1653,48],[0.17161,49],[0.17813,50],
                               [0.18487,51],[0.19184,52],[0.19903,53],[0.20646,54],[0.21414,55],[0.22206,56],
                               [0.23024,57],[0.23868,58],[0.2474,59],[0.25639,60],[0.26567,61],[0.27524,62],
                               [0.28511,63],[0.29529,64],[0.30579,65],[0.31662,66],[0.32777,67],[0.33927,68],
                               [0.35113,69],[0.36334,70],[0.37592,71],[0.38889,72],[0.40224,73],[0.41599,74],
                               [0.43015,75],[0.44473,76],[0.45973,77],[0.47518,78],[0.49108,79],[0.50744,80],
                               [0.52427,81],[0.54159,82],[0.5594,83],[0.57772,84],[0.59656,85],[0.61593,86],
                               [0.63585,87],[0.65632,88],[0.67736,89],[0.69899,90],[0.72122,91],[0.74405,92],
                               [0.76751,93],[0.79161,94],[0.81636,95],[0.84178,96],[0.86788,97],[0.89468,98],
                               [0.9222,99],[0.95044,100],[0.97943,101],[1.00917,102],[1.0397,103],[1.07102,104],
                               [1.10315,105],[1.13611,106],[1.16992,107],[1.20459,108],[1.24014,109],[2,126.04],
                               [3,141.43],[4,152.93],[5,162.21],[6,170.03],[8,182.84],[10,193.19],[14.696,211.99],
                               [15,213.03],[20,227.96],[25,240.08],[30,250.3],[35,259.25],[40,267.22],[45,274.41],
                               [50,280.99],[55,287.05],[60,292.69],[65,297.95],[70,302.91],[75,307.59],[80,312.02],
                               [85,316.24],[90,320.26],[95,324.11],[100,327.81],[110,334.77],[120,341.25],[130,347.32],
                               [140,353.03],[150,358.42],[160,363.54],[170,368.41],[180,373.07],[190,377.52],[200,381.8],
                               [250,400.97],[300,417.35],[350,431.74],[400,444.62],[450,456.31],[500,467.04],[550,476.97],
                               [600,486.24]]