__author__ = 'cao'
from primary_signal.signal_source import signal_source
from primary_signal.get_primary_signal import priamry_signal
from util.Tool import show_Data, show_complex, show_data_cursor
from primary_signal.ADC import AD
import numpy as np





# 变频测试
def complex_ad_test(primary_data):
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.first_complex_ad(1,primary_data)
    ad_test.second_complex_ad(1)
    show_complex(ad_test.second_complex_signal_current)


# 检测有效信号测试
def detect_wave_test(primary_data):
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.first_complex_ad(1, primary_data)
    ad_test.second_complex_ad(1)
    ad_test.detect_wave(ad_test.second_complex_signal_current)
    primary_data_abs = np.abs(ad_test.second_complex_signal_current)
    show_data_cursor(primary_data_abs, ad_test.check_result)

def cul_param_test(primary_data,frist_index, second_index ):
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.first_complex_ad(frist_index, primary_data)
    ad_test.second_complex_ad(second_index)
    show_complex(ad_test.second_complex_signal_current)
    # ad_test.detect_wave(ad_test.second_complex_signal_current)
    # print(ad_test.check_result)
    ad_test.cul_param(ad_test.second_complex_signal_current, frist_index, second_index)

def fullFlowTest(primary_data):
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.AD_data()


# 本文件对ADC进行测试
if __name__ == "__main__":
    # 首先获取原始信号
    signal = signal_source(2, 30, 2, [70, 10], 3, [17, 10, 0.4])
    # test_signal_2 = signal_source(3, 30, 4, [100, 8, 0.2], 2, [23, 0.4])
    signals = [signal]
    simutime = 500
    frame_time = 100
    priamry_signal_test = priamry_signal(signals, simutime)
    # 获取原始信号
    primary_data = priamry_signal_test.primary_data
    show_Data(primary_data)
    cul_param_test(primary_data, 0, 2)