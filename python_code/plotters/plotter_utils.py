from python_code.plotters.plotter_config import COLORS_DICT, LINESTYLES_DICT, MARKERS_DICT
from python_code.utils.config_singleton import Config
from python_code.utils.python_utils import load_pkl, save_pkl
from python_code.vnet.trainer import Trainer
from dir_definitions import FIGURES_DIR, PLOTS_DIR
import datetime
import os
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import math

conf = Config()

MIN_BER_COEF = 0.2
MARKER_EVERY = 10


def get_ser_plot(dec: Trainer, run_over: bool, method_name: str, trial=None):
    print(method_name)
    # set the path to saved plot results for a single method (so we do not need to run anew each time)
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
    file_name = '_'.join([method_name, str(conf.channel_type)])
    if trial is not None:
        file_name = file_name + '_' + str(trial)
    plots_path = os.path.join(PLOTS_DIR, file_name + '.pkl')
    print(plots_path)
    # if plot already exists, and the run_over flag is false - load the saved plot
    if os.path.isfile(plots_path) and not run_over:
        print("Loading plots")
        ser_total = load_pkl(plots_path)
    else:
        # otherwise - run again
        print("calculating fresh")
        ser_total = dec.evaluate()
        save_pkl(plots_path, ser_total)
    print(np.mean(ser_total))
    return ser_total


def plot_by_values(all_curves: List[Tuple[np.ndarray, np.ndarray, str]], field_name, values: List[float]):
    # path for the saved figure
    current_day_time = datetime.datetime.now()
    folder_name = f'{current_day_time.month}-{current_day_time.day}-{current_day_time.hour}-{current_day_time.minute}'
    if not os.path.isdir(os.path.join(FIGURES_DIR, folder_name)):
        os.makedirs(os.path.join(FIGURES_DIR, folder_name))

    plt.figure()
    names = []
    for i in range(len(all_curves)):
        if all_curves[i][1] not in names:
            names.append(all_curves[i][1])

    for method_name in names:
        mean_sers = []
        for ser, cur_name in all_curves:
            mean_ser = np.mean(ser)
            if cur_name != method_name:
                continue
            mean_sers.append(mean_ser)
        plt.plot(values, mean_sers, label=method_name,
                 color=COLORS_DICT[method_name], marker=MARKERS_DICT[method_name],
                 linestyle=LINESTYLES_DICT[method_name], linewidth=2.2)

    plt.xticks(values, values)
    plt.xlabel(field_name)
    plt.ylabel('BER')
    plt.grid(which='both', ls='--')
    plt.legend(loc='lower left', prop={'size': 15})
    plt.yscale('log')
    plt.savefig(os.path.join(FIGURES_DIR, folder_name, f'coded_ber_versus_snrs.png'),
                bbox_inches='tight')
    plt.show()
