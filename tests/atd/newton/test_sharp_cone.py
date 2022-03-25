import numpy as np
from pygasflow.atd.newton.sharp_cone import sharp_cone_solver
from pytest import raises

alpha = np.deg2rad([1, 2, 4, 6, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

def pprint(arr):
    s = ["{:.8f}".format(t) for t in arr]
    print("[%s]" % ", ".join(s))


def test_phi1_0_phi2_360_beta_0_theta_c_2_5():
    theta_c = np.deg2rad(2.5)
    beta = np.deg2rad(0)
    res1 = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)
    res2 = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=False)
    assert len(res1) == len(res2)


def test_single_alpha_multiple_beta():
    alpha = np.deg2rad(25)
    theta_c = np.deg2rad(2.5)
    beta = np.deg2rad([5, 10, 15])
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)
    assert len(res["CA"]) == 3


def test_multiple_alpha_multiple_beta_1():
    theta_c = np.deg2rad(2.5)
    alpha = np.deg2rad([2, 4, 6])
    beta = np.deg2rad([5, 10, 15])
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)
    assert len(res["CA"]) == 3


def test_multiple_alpha_multiple_beta_2():
    theta_c = np.deg2rad(2.5)
    beta = np.deg2rad([5, 10, 15])
    raises(ValueError, lambda: sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True))


###############################################################################
################################ FULL CONE ####################################
###############################################################################


def test_phi1_0_phi2_360_beta_0_theta_c_2_5():
    theta_c = np.deg2rad(2.5)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.0348331, 0.06962375, 0.14333589, 0.23680353, 0.35246338, 0.49000844,
        0.64882907, 0.92527287, 1.48018787, 2.13793112, 2.87852706, 3.67947641,
        4.51644417, 5.36400023, 6.19639239, 6.98832908, 7.71574783, 8.35654649,
        8.89125477, 9.30362588, 9.58113015, 9.71533577]))
    assert np.allclose(res["CA"], np.array(
        [0.0041081, 0.0050163, 0.0084390, 0.0132699, 0.0193024, 0.0264792,
        0.0347563, 0.0491379, 0.0779330, 0.1119791, 0.1502378, 0.1915450,
        0.2346448, 0.2782270, 0.3209671, 0.3615662, 0.3987905, 0.4315088,
        0.4587269, 0.4796178, 0.4935465, 0.5000897]))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [7.37069127, 9.32491114, 7.73186168, 6.16915604, 5.08078299,
        4.29957043, 3.71485661, 3.07040407, 2.35426599, 1.88086432,
        1.54058864, 1.28086316, 1.07334335, 0.90137689, 0.75450633,
        0.62579773, 0.51043342, 0.40492043, 0.30661938, 0.21344906,
        0.12369115, 0.03585294]
    ))


def test_phi1_0_phi2_360_beta_0_theta_c_10():
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.0338471, 0.0676531, 0.1349765, 0.2016424, 0.2673259, 0.3317070,
        0.3958161, 0.4965648, 0.6789799, 0.8767513, 1.0845633, 1.2963321,
        1.5057194, 1.7064098, 1.8923307, 2.0578475, 2.1979402, 2.3083580,
        2.3857497, 2.4277665, 2.4331334, 2.4016885]))
    assert np.allclose(res["CA"], np.array(
        [0.0605844, 0.0614152, 0.0647332, 0.0702452, 0.0779244, 0.0877333,
        0.0993813, 0.1190748, 0.1561021, 0.1967785, 0.2396015, 0.2831558,
        0.3260587, 0.3669718, 0.4046294, 0.4378715, 0.4656765, 0.4871905,
        0.5017525, 0.5089138, 0.5084514, 0.5003742]))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [0.53599554, 1.02713680, 1.75875754, 2.12447708, 2.21979524,
        2.16271654, 2.04175513, 1.84294088, 1.54294719, 1.29619122,
        1.09292822, 0.92207878, 0.77516070, 0.64601612, 0.53015296,
        0.42422106, 0.32564670, 0.23238236, 0.14273215, 0.05522508,
        -0.03148275, -0.11869057]
    ))


def test_phi1_0_phi2_360_beta_0_theta_c_45():
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.0174497, 0.0348782, 0.0695866, 0.1039558, 0.1378187, 0.1710101,
        0.2033683, 0.2500000, 0.3213938, 0.3830222, 0.4330127, 0.4698463,
        0.4924039, 0.5000000, 0.4938414, 0.4775138, 0.4529470, 0.4216144,
        0.3848985, 0.3441857, 0.3008861, 0.2564231]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.9998477, 0.9993910, 0.9975670, 0.9945369, 0.9903154, 0.9849232,
        0.9783864, 0.9665064, 0.9415111, 0.9106969, 0.8750000, 0.8355050,
        0.7934120, 0.7500000, 0.7051163, 0.6564791, 0.6037551, 0.5474289,
        0.4883984, 0.4278132, 0.3669718, 0.3072435]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [-0.00000266, -0.00002125, -0.00016972, -0.00057108, -0.00134802,
        -0.00261897, -0.00449693, -0.00868375, -0.02011189, -0.03822877,
        -0.06415003, -0.09891036, -0.14366783, -0.20000000, -0.26783326,
        -0.34371038, -0.42699349, -0.51829631, -0.61903492, -0.73142078,
        -0.85865265, -1.00531587]
    ))


def test_phi1_0_phi2_360_beta_0_theta_c_90():
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.9993908, 1.9975641, 1.9902681, 1.9781476, 1.9612617, 1.9396926,
        1.9135455, 1.8660254, 1.7660444, 1.6427876, 1.5000000, 1.3420201,
        1.1736482, 1.0000000, 0.8263518, 0.6579799, 0.5000000, 0.3572124,
        0.2339556, 0.1339746, 0.0603074, 0.0151922]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [-0.01745506, -0.03492077, -0.06992681, -0.10510424, -0.14054083,
        -0.17632698, -0.21255656, -0.26794919, -0.36397023, -0.46630766,
        -0.57735027, -0.70020754, -0.83909963, -1.00000000, -1.19175359,
        -1.42814801, -1.73205081, -2.14450692, -2.74747742, -3.73205081,
        -5.67128182, -11.43005230]
    ))


def test_phi1_0_phi2_360_beta_15_theta_c_2_5():
    theta_c = np.deg2rad(2.5)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.06050139, 0.12118246, 0.24611445, 0.37824135, 0.52041054,
        0.67478726, 0.84285279, 1.12238482, 1.66245039, 2.28899408,
        2.98788132, 3.74030417, 4.52468279, 5.31790550, 6.09629979,
        6.83648236, 7.51613687, 8.11472853, 8.61414864, 8.99927693,
        9.25844834, 9.38381186]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.04929960, 0.04981057, 0.05181991, 0.05513730, 0.05972097,
        0.06551928, 0.07247487, 0.08494503, 0.11063186, 0.14155282,
        0.17661712, 0.21466559, 0.25448171, 0.29481481, 0.33441037,
        0.37204375, 0.40655480, 0.43688149, 0.46209115, 0.48140813,
        0.49423690, 0.50017976]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.92655353, -0.93036394, -0.94537704, -0.96958724, -1.00194349,
        -1.04123582, -1.08623870, -1.16197827, -1.30241522, -1.45127215,
        -1.60120077, -1.74730240, -1.88613639, -2.01515319, -2.13238099,
        -2.23625142, -2.32550084, -2.39911318, -2.45628636, -2.49641217,
        -2.51906400, -2.52398935]
    ))


def test_phi1_0_phi2_360_beta_15_theta_c_45():
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.01628084, 0.03254184, 0.06492514, 0.09699212, 0.12858658,
        0.15955457, 0.18974523, 0.23325318, 0.29986450, 0.35736460,
        0.40400635, 0.43837258, 0.45941907, 0.46663391, 0.46210326,
        0.44823017, 0.42651338, 0.39827157, 0.36479559, 0.32739419,
        0.28739946, 0.24615216]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.96636426, 0.96593816, 0.96423635, 0.96140921, 0.95747052,
        0.95243946, 0.94634055, 0.93525635, 0.91193547, 0.88318543,
        0.84987976, 0.81303046, 0.77375716, 0.73311549, 0.68981754,
        0.64257460, 0.59141428, 0.53688980, 0.47987313, 0.42144414,
        0.36281031, 0.30523958]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.24996192, -0.24984771, -0.24939101, -0.24863047, -0.24756702,
        -0.24620194, -0.24453690, -0.24148146, -0.23492316, -0.22657695,
        -0.21650635, -0.20478801, -0.19151111, -0.17682503, -0.16163579,
        -0.14661858, -0.13196370, -0.11774868, -0.10401985, -0.09081961,
        -0.07819643, -0.06620822]
    ))


def test_phi1_0_phi2_360_beta_15_theta_c_90():
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.86545704, 1.86375263, 1.85694539, 1.84563684, 1.82988207,
        1.80975785, 1.78536222, 1.74102540, 1.64774190, 1.53274171,
        1.39951905, 1.25212184, 1.09502866, 0.93301270, 0.77099675,
        0.61390356, 0.46650635, 0.33328370, 0.21828351, 0.12500000,
        0.05626755, 0.01417456]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))


###############################################################################
############################# PHI_1=90, PHI_2=270 #############################
###############################################################################


def test_phi1_90_phi2_270_beta_0_theta_c_10():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.2529397, 0.2908111, 0.3743719, 0.4680121, 0.5712755, 0.6836590,
        0.8046151, 1.0008230, 1.3618146, 1.7556653, 2.1704080, 2.5934412,
        3.0119110, 3.4131025, 3.7848258, 4.1157861, 4.3959275, 4.6167379,
        4.7715082, 4.8555358, 4.8662674, 4.8033771]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.0681833, 0.0766037, 0.0950363, 0.1155152, 0.1379408, 0.1622037,
        0.1881858, 0.2301033, 0.3066617, 0.3895527, 0.4762577, 0.5641422,
        0.6505358, 0.7328136, 0.8084756, 0.8752228, 0.9310272, 0.9741931,
        1.0034090, 1.0177871, 1.0168907, 1.0007469]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [3.46770085, 3.32110555, 3.03367257, 2.76779849, 2.52895331,
        2.31672951, 2.12858962, 1.88484410, 1.55822639, 1.30274046,
        1.09604638, 0.92367317, 0.77601609, 0.64648893, 0.53041788,
        0.42436907, 0.32572758, 0.23242447, 0.14275220, 0.05523320,
        -0.03148037, -0.11869026]
    ))


def test_phi1_90_phi2_270_beta_0_theta_c_45():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.6540049, 0.6712395, 0.7051737, 0.7382570, 0.7703282, 0.8012310,
        0.8308150, 0.8724046, 0.9331901, 0.9817406, 1.0165808, 1.0366523,
        1.0413450, 1.0305165, 1.0044957, 0.9640733, 0.9104775, 0.8453368,
        0.7706304, 0.6886283, 0.6018221, 0.5128492]
    ))
    assert np.allclose(res["CA"], np.array(
        [1.0220654, 1.0437994, 1.0861674, 1.1268976, 1.1657916, 1.2026599,
        1.2373230, 1.2848162, 1.3507224, 1.3983759, 1.4263289, 1.4337319,
        1.4203601, 1.3866198, 1.3335360, 1.2627219, 1.1763289, 1.0769821,
        0.9677002, 0.8518035, 0.7328136, 0.6143459]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [0.61555519, 0.59479548, 0.55414685, 0.51458668, 0.47602910,
        0.43839030, 0.40158893, 0.34778571, 0.26122437, 0.17760622,
        0.09590923, 0.01516127, -0.06559227, -0.14732446, -0.23106761,
        -0.31796208, -0.40931783, -0.50669678, -0.61202922, -0.72778834,
        -0.85727024, -1.00508282]
    ))


def test_phi1_90_phi2_270_beta_0_theta_c_90():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.9993908, 1.9975641, 1.9902681, 1.9781476, 1.9612617, 1.9396926,
        1.9135455, 1.8660254, 1.7660444, 1.6427876, 1.5000000, 1.3420201,
        1.1736482, 1.0000000, 0.8263518, 0.6579799, 0.5000000, 0.3572124,
        0.2339556, 0.1339746, 0.0603074, 0.0151922]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [-0.01745506, -0.03492077, -0.06992681, -0.10510424, -0.14054083,
        -0.17632698, -0.21255656, -0.26794919, -0.36397023, -0.46630766,
        -0.57735027, -0.70020754, -0.83909963, -1.00000000, -1.19175359,
        -1.42814801, -1.73205081, -2.14450692, -2.74747742, -3.73205081,
        -5.67128182, -11.43005230]
    ))


def test_phi1_90_phi2_270_beta_15_theta_c_10():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.38990594, 0.42574127, 0.50437497, 0.59213840, 0.68872645,
        0.79373527, 0.90668988, 1.08984900, 1.42673879, 1.79424078,
        2.18121263, 2.57590531, 2.96632932, 3.34062208, 3.68740944,
        3.99615166, 4.25746370, 4.46340028, 4.60769708, 4.68596070,
        4.69580168, 4.63690649]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.12670750, 0.13479488, 0.15233509, 0.17167369, 0.19275683,
        0.21550692, 0.23982885, 0.27901852, 0.35051537, 0.42787016,
        0.50874964, 0.59070213, 0.67123778, 0.74790644, 0.81837298,
        0.88048865, 0.93235644, 0.97238863, 0.99935497, 1.01241976,
        1.01116701, 0.99561267]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.51541995, -0.53437155, -0.57237119, -0.61024103, -0.64774737,
        -0.68472225, -0.72104202, -0.77409063, -0.85811002, -0.93590456,
        -1.00679003, -1.07019270, -1.12562326, -1.17266854, -1.21098949,
        -1.24032144, -1.26047511, -1.27133768, -1.27287376, -1.26512598,
        -1.24821531, -1.22234112]
    ))


def test_phi1_90_phi2_270_beta_15_theta_c_45():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.62441001, 0.64049017, 0.67215120, 0.70301831, 0.73294113,
        0.76177388, 0.78937608, 0.82817974, 0.88489338, 0.93019158,
        0.96269797, 0.98142486, 0.98580326, 0.97570011, 0.95142240,
        0.91370780, 0.86370225, 0.80292513, 0.73322314, 0.65671412,
        0.57572079, 0.49268401]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.98709366, 1.00737171, 1.04690160, 1.08490342, 1.12119203,
        1.15559065, 1.18793168, 1.23224352, 1.29373482, 1.33819616,
        1.36427663, 1.37118376, 1.35870769, 1.32722751, 1.27769972,
        1.21162919, 1.13102345, 1.03833166, 0.93637022, 0.82823709,
        0.71713428, 0.60610501]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.25181368, -0.25355066, -0.25679240, -0.25972129, -0.26233374,
        -0.26462658, -0.26659702, -0.26894301, -0.27121262, -0.27141814,
        -0.26955800, -0.26564636, -0.25971299, -0.25180305, -0.24197674,
        -0.23030884, -0.21688815, -0.20181681, -0.18520952, -0.16719275,
        -0.14798715, -0.12806874]
    ))


def test_phi1_90_phi2_270_beta_15_theta_c_90():
    phi_1 = np.deg2rad(90)
    phi_2 = np.deg2rad(270)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.86545704, 1.86375263, 1.85694539, 1.84563684, 1.82988207,
        1.80975785, 1.78536222, 1.74102540, 1.64774190, 1.53274171,
        1.39951905, 1.25212184, 1.09502866, 0.93301270, 0.77099675,
        0.61390356, 0.46650635, 0.33328370, 0.21828351, 0.12500000,
        0.05626755, 0.01417456]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))


###############################################################################
############################ PHI_1=150, PHI_2=210 #############################
###############################################################################


def test_phi1_150_phi2_210_beta_0_theta_c_10():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.3912772, 0.4615374, 0.6184732, 0.7966481, 0.9951940, 1.2131437,
        1.4494352, 1.8357223, 2.5537767, 3.3454893, 4.1868041, 5.0521584,
        5.9152587, 6.7498802, 7.5306634, 8.2338845, 8.8381764, 9.3251782,
        9.6800925, 9.8921355, 9.9548642, 9.8663727]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.0722271, 0.0851749, 0.1140906, 0.1469136, 0.1834841, 0.2236238,
        0.2671373, 0.3382651, 0.4704638, 0.6162030, 0.7710546, 0.9303135,
        1.0891407, 1.2427102, 1.3863561, 1.5157136, 1.6268523, 1.7163953,
        1.7816219, 1.8205502, 1.8319974, 1.8156157]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [4.93336806, 4.52713379, 3.88013984, 3.38705699, 2.99801600,
        2.68256475, 2.42106182, 2.10214304, 1.70186126, 1.40525069,
        1.17354930, 0.98497562, 0.82631178, 0.68903443, 0.56736217,
        0.45719458, 0.35549911, 0.25993725, 0.16862422, 0.07996565,
        -0.00746128, -0.09500241]
    ))


def test_phi1_150_phi2_210_beta_0_theta_c_45():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.9867860, 1.0185550, 1.0816766, 1.1439868, 1.2051821, 1.2649644,
        1.3230423, 1.4063473, 1.5328052, 1.6404957, 1.7261466, 1.7871556,
        1.8216688, 1.8286376, 1.8078503, 1.7599385, 1.6863579, 1.5893443,
        1.4718453, 1.3374312, 1.1901860, 1.0345837]
    ))
    assert np.allclose(res["CA"], np.array(
        [1.0333002, 1.0665072, 1.1324796, 1.1975959, 1.2615388, 1.3239968,
        1.3846656, 1.4716702, 1.6036980, 1.7160685, 1.8053675, 1.8688816,
        1.9046810, 1.9116780, 1.8896599, 1.8392957, 1.7621158, 1.6604653,
        1.5374326, 1.3967561, 1.2427102, 1.0799756]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    assert np.allclose(res["L/D"], np.array(
        [0.92215798, 0.89042125, 0.82979153, 0.77256666, 0.71834010,
        0.66676056, 0.61752245, 0.54747880, 0.43907742, 0.33867989,
        0.24404970, 0.15336874, 0.06508471, -0.02220144, -0.10982685,
        -0.19914960, -0.29163444, -0.38895305, -0.49311429, -0.60664722,
        -0.73287553, -0.87635116]
    ))


def test_phi1_150_phi2_210_beta_0_theta_c_90():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.9993908, 1.9975641, 1.9902681, 1.9781476, 1.9612617, 1.9396926,
        1.9135455, 1.8660254, 1.7660444, 1.6427876, 1.5000000, 1.3420201,
        1.1736482, 1.0000000, 0.8263518, 0.6579799, 0.5000000, 0.3572124,
        0.2339556, 0.1339746, 0.0603074, 0.0151922]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
    # assert np.allclose(res["L/D"], np.array())


def test_phi1_150_phi2_210_beta_15_theta_c_10():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.42370696, 0.48926061, 0.63568374, 0.80192319, 0.98716906,
        1.19051884, 1.41098185, 1.77139258, 2.44134649, 3.18002435,
        3.96498181, 4.77236834, 5.57765191, 6.35636438, 7.08484497,
        7.74095916, 8.30477126, 8.75915012, 9.09028967, 9.28812840,
        9.34665509, 9.26409142]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.07862856, 0.09070904, 0.11768777, 0.14831209, 0.18243280,
        0.21988368, 0.26048226, 0.32684544, 0.45018846, 0.58616501,
        0.73064353, 0.87923410, 1.02742187, 1.17070423, 1.30472763,
        1.42541982, 1.52911364, 1.61265840, 1.67351564, 1.70983624,
        1.72051662, 1.70523226]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.09152103, -0.09911926, -0.11422282, -0.12918722, -0.14399422,
        -0.15862579, -0.17306410, -0.19432079, -0.22853689, -0.26101368,
        -0.29150400, -0.31977580, -0.34561392, -0.36882170, -0.38922253,
        -0.40666114, -0.42100481, -0.43214438, -0.43999507, -0.44449714,
        -0.44561631, -0.44334407]
    ))


def test_phi1_150_phi2_210_beta_15_theta_c_45():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [0.92601455, 0.95565547, 1.01454869, 1.07268491, 1.12978090,
        1.18555850, 1.23974596, 1.31747059, 1.43545741, 1.53593398,
        1.61584740, 1.67276951, 1.70497078, 1.71147278, 1.69207796,
        1.64737561, 1.57872400, 1.48820907, 1.37858106, 1.25317098,
        1.11578934, 0.97061041]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.96987685, 1.00085936, 1.06241248, 1.12316680, 1.18282634,
        1.24110044, 1.29770520, 1.37888162, 1.50206521, 1.60690836,
        1.69022544, 1.74948492, 1.78288623, 1.78941447, 1.76887131,
        1.72188092, 1.64987109, 1.55502980, 1.44023876, 1.30898583,
        1.16525907, 1.01342554]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.04393949, -0.04461392, -0.04592183, -0.04717378, -0.04836826,
        -0.04950382, -0.05057905, -0.05207598, -0.05425182, -0.05601477,
        -0.05735141, -0.05825157, -0.05870840, -0.05871843, -0.05828157,
        -0.05740116, -0.05608389, -0.05433978, -0.05218212, -0.04962732,
        -0.04669483, -0.04340696]
    ))


def test_phi1_150_phi2_210_beta_15_theta_c_90():
    phi_1 = np.deg2rad(150)
    phi_2 = np.deg2rad(210)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.86545704, 1.86375263, 1.85694539, 1.84563684, 1.82988207,
        1.80975785, 1.78536222, 1.74102540, 1.64774190, 1.53274171,
        1.39951905, 1.25212184, 1.09502866, 0.93301270, 0.77099675,
        0.61390356, 0.46650635, 0.33328370, 0.21828351, 0.12500000,
        0.05626755, 0.01417456]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))


###############################################################################
############################# PHI_1=-90, PHI_2=90 #############################
###############################################################################

# NOTE: here, tables CY for beta=0 are missing

def test_phi1_90_phi2_90_beta_0_theta_c_10():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [-0.18524536, -0.15550498, -0.10441887, -0.06472734, -0.03662376,
        -0.02024506, -0.01298298, -0.00769332, -0.00385472, -0.00216276,
        -0.00128146, -0.00077706, -0.00047229, -0.00028296, -0.00016448,
        -0.00009114, -0.00004706, -0.00002192, -0.00000875, -0.00000271,
        -0.00000053, -0.00000003]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.05298551, 0.04622662, 0.03443006, 0.02497516, 0.01790799,
        0.01326297, 0.01057683, 0.00804637, 0.00554239, 0.00400424,
        0.00294532, 0.00216942, 0.00158165, 0.00113005, 0.00078320,
        0.00052022, 0.00032588, 0.00018800, 0.00009610, 0.00004051,
        0.00001200, 0.00000150]
    ))
    # NOTE: L/D for this case produces different results. However, CL and CD
    # produces the correct results...
    assert np.allclose(res["CL"], np.array(
        [-0.18614187, -0.15702354, -0.10656623, -0.06698337, -0.03875965,
        -0.02224058, -0.01489832, -0.00951373, -0.00551786, -0.00365239,
        -0.00258244, -0.00188086, -0.00137846, -0.00099914, -0.00070569,
        -0.00047841, -0.00030575, -0.00017965, -0.00009329, -0.00003983,
        -0.00001191, -0.00000150]
    ))
    assert np.allclose(res["CD"], np.array(
        [0.04974446, 0.04077142, 0.02706230, 0.01807249, 0.01263666,
        0.00954596, 0.00764639, 0.00578102, 0.00388975, 0.00271505,
        0.00190999, 0.00133138, 0.00090803, 0.00059899, 0.00037744,
        0.00022373, 0.00012218, 0.00005958, 0.00002465, 0.00000786,
        0.00000156, 0.00000010]
    ))


def test_phi1_90_phi2_90_beta_0_theta_c_45():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [-0.61910539, -0.60148307, -0.56600063, -0.53034532, -0.49469083,
        -0.45921089, -0.42407834, -0.37240463, -0.29040251, -0.21569614,
        -0.15055542, -0.09695963, -0.05653724, -0.03051648, -0.01681284,
        -0.00904582, -0.00458353, -0.00210800, -0.00083342, -0.00025702,
        -0.00004989, -0.00000309]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.97763000, 0.95498266, 0.90896667, 0.86217621, 0.81483923,
        0.76718637, 0.71944978, 0.64819646, 0.53229981, 0.42301786,
        0.32367110, 0.23727813, 0.16646396, 0.11338023, 0.07669657,
        0.05023624, 0.03118132, 0.01787557, 0.00909663, 0.00382283,
        0.00113005, 0.00014108]
    ))
    assert np.allclose(res["L/D"], np.array(
        [-0.65800014, -0.67970715, -0.72414358, -0.77001115, -0.81738465,
        -0.86632682, -0.91688182, -0.99576485, -1.13488420, -1.28072299,
        -1.42525883, -1.55327566, -1.64855649, -1.73654588, -1.90993004,
        -2.16495408, -2.52087318, -3.02826410, -3.79415642, -5.07190214,
        -7.62456162, -15.27119603]
    ))


def test_phi1_90_phi2_90_beta_0_theta_c_90():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(0)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.99939083, 1.99756405, 1.99026807, 1.97814760, 1.96126170,
        1.93969262, 1.91354546, 1.86602540, 1.76604444, 1.64278761,
        1.50000000, 1.34202014, 1.17364818, 1.00000000, 0.82635182,
        0.65797986, 0.50000000, 0.35721239, 0.23395556, 0.13397460,
        0.06030738, 0.01519225]
    ))
    assert np.allclose(res["L/D"], np.array(
        [-0.01745506, -0.03492077, -0.06992681, -0.10510424, -0.14054083,
        -0.17632698, -0.21255656, -0.26794919, -0.36397023, -0.46630766,
        -0.57735027, -0.70020754, -0.83909963, -1.00000000, -1.19175359,
        -1.42814801, -1.73205081, -2.14450692, -2.74747742, -3.73205081,
        -5.67128182, -11.43005230]
    ))


def test_phi1_90_phi2_90_beta_15_theta_c_10():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(10)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [-0.32521021, -0.29630911, -0.24516572, -0.20237511, -0.16708916,
        -0.13830189, -0.11496746, -0.08806294, -0.05830691, -0.04013515,
        -0.02856183, -0.02087881, -0.01558791, -0.01182987, -0.00909166,
        -0.00705472, -0.00551402, -0.00433316, -0.00341876, -0.00270514,
        -0.00214504, -0.00170371]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.11189311, 0.10515537, 0.09296862, 0.08239895, 0.07329264,
        0.06547456, 0.05876568, 0.05041692, 0.03992423, 0.03234634,
        0.02666241, 0.02225310, 0.01873599, 0.01586764, 0.01348780,
        0.01148748, 0.00979014, 0.00834039, 0.00709694, 0.00602815,
        0.00510906, 0.00431946]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.47786251, -0.45937465, -0.42330569, -0.38888166, -0.35655798,
        -0.32664940, -0.29930168, -0.26303462, -0.21396197, -0.17623665,
        -0.14681206, -0.12340112, -0.10440788, -0.08873526, -0.07562291,
        -0.06453436, -0.05508270, -0.04698205, -0.04001583, -0.03401575,
        -0.02884765, -0.02440195]
    ))


def test_phi1_90_phi2_90_beta_15_theta_c_45():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(45)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.array(
        [-0.59184834, -0.57540649, -0.54230093, -0.50903406, -0.47576798,
        -0.44266474, -0.40988562, -0.36167339, -0.28516438, -0.21546238,
        -0.15468527, -0.10467971, -0.06696511, -0.04243229, -0.02721587,
        -0.01724746, -0.01067548, -0.00638199, -0.00363195, -0.00192574,
        -0.00092187, -0.00037968]
    ))
    assert np.allclose(res["CA"], np.array(
        [0.94563485, 0.92450460, 0.88157110, 0.83791500, 0.79374900,
        0.74928828, 0.70474943, 0.63826918, 0.53013613, 0.42817469,
        0.33548290, 0.25487716, 0.18880664, 0.13900346, 0.10193537,
        0.07352002, 0.05180511, 0.03544793, 0.02337603, 0.01465118,
        0.00848635, 0.00437415]
    ))
    assert np.allclose(res["CY"], np.array(
        [-0.24811017, -0.24614476, -0.24198962, -0.23753966, -0.23280029,
        -0.22777729, -0.22247678, -0.21401990, -0.19863369, -0.18173576,
        -0.16345470, -0.14392966, -0.12330923, -0.10184701, -0.08129483,
        -0.06292833, -0.04703925, -0.03368055, -0.02283018, -0.01444647,
        -0.00840572, -0.00434770]
    ))


def test_phi1_90_phi2_90_beta_15_theta_c_90():
    phi_1 = np.deg2rad(-90)
    phi_2 = np.deg2rad(90)
    theta_c = np.deg2rad(90)
    beta = np.deg2rad(15)
    res = sharp_cone_solver(1, theta_c, alpha, beta, phi_1=phi_1, phi_2=phi_2, to_dict=True)

    assert np.allclose(res["CN"], np.zeros_like(res["CN"]))
    assert np.allclose(res["CA"], np.array(
        [1.86545704, 1.86375263, 1.85694539, 1.84563684, 1.82988207,
        1.80975785, 1.78536222, 1.74102540, 1.64774190, 1.53274171,
        1.39951905, 1.25212184, 1.09502866, 0.93301270, 0.77099675,
        0.61390356, 0.46650635, 0.33328370, 0.21828351, 0.12500000,
        0.05626755, 0.01417456]
    ))
    assert np.allclose(res["CY"], np.zeros_like(res["CY"]))
