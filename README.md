# data-augmentations-receivers

*"“Would you tell me, please, which way I ought to go from here?” “That depends a good deal on where you want to get to,” said the Cat. “I don't much care where—” said Alice. “Then it doesn't matter which way you go,” said the Cat."* 

--Alice in Wonderland.

# Data Augmentation for Deep Receivers

Python repository for the paper "Data Augmentation for Deep Receivers".

Please cite our [paper](https://ieeexplore.ieee.org/abstract/document/9833983/), if the code is used for publishing research.

# Table of Contents

- [Introduction](#introduction)
- [Folders Structure](#folders-structure)
  * [python_code](#python_code)
    + [augmentations](#augmentations)
    + [channel](#channel)
    + [plotters](#plotters)
    + [utils](#utils)
    + [vnet](#vnet)
  * [resources](#resources)
  * [dir_definitions](#dir_definitions)
- [Execution](#execution)
  * [Environment Installation](#environment-installation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction

This repository implements the proposed augmentation scheme for [ViterbiNet](https://ieeexplore.ieee.org/document/8815457), a machine-learning model-based detector, for the a channel with memory of L. Our proposed novel method incorporates (1) spatial and temporal clustering (2) takes into account classes diversity and (3) keeps low complexity, tailored for online communication scenarios. We explain on the different directories and subdirectories below.

# Folders Structure

## python_code 

The python simulations of the simplified communication chain: symbols generation, channel transmission and detection.

### augmentations

The proposed augmentation scheme, and the three baselines: regular training (no augmentations applied), partial-knowledge genie and full-knowledge genie. See the paper for more details on these augmentation methods. Algorithm 1 specifies our proposed self-supervised augmentation scheme.

### channel 

Includes all relevant channel functions and classes. The class in "channel_dataset.py" implements the main class for aggregating pairs of (transmitted,received) samples. 
In "channel.py", the ISI AWGN channel is implemented. "channel_estimation.py" is for the calculation of the h values. Lastly, the channel BPSK modulator lies in "channel_modulator.py".

### plotters

Plotting of the BER versus SNR, for Figures 3 and 4 in the paper.

### vnet 

Includes three files:

(1) The backbone detector in "vnet_detector.py" module;

(2) A basic "trainer.py" class, includes the main evaluation function. It is also used for parsing the config.yaml file and preparing the deep learning setup (loss, optimizer, ...).

(3) The ViterbiNet trainer, in "vnet_trainer.py", which inherets from the basic trainer class, extending it as needed.

### utils

Extra utils for saving and loading pkls; calculating the accuracy over FER and BER; and transitioning over the trellis.

### config

Controls all parameters and hyperparameters.

## resources

Keeps the channel coefficients vectors (4 taps, each with 300 blocks).

## dir_definitions 

Definitions of relative directories.

# Execution

To execute the code, first download and install Git, Anaconda and PyCharm.

Then install the environment, follow the installation setup below. 

At last, open PyCharm in the root directory. You may run either the trainers or one of the plotters.

This code was simulated with GeForce RTX 2060 with driver version 432.00 and CUDA 10.1. 

## Environment Installation

1. Open git bash and cd to a working directory of you choice.

2. Clone this repository to your local machine.

3. Open Anaconda prompt and navigate to the cloned repository.

4. Run the command "conda env create -f environment.yml". This should install the required python environment.

5. Open the cloned directory using PyCharm.

6. After the project has been opened in PyCharm, go to settings, File -> Settings... (or CTRL ALT S)

7. In the opened window open the tab Project -> Project Interpreter

8. In the new window, click on the cog icon and then on Add...

9. In the add python interpreter window, click on the Conda Environment tab

10. Select Existing environment and navigate to where the python.exe executable of the deep_ensemble environment is installed under the interpreter setting

  - For windows its usually found at C:\users\<username>\anaconda3\envs\environment\python.exe)

  - For linux its usually found at /home/<username>/anaconda3
  
11. Click OK

12. Done!
