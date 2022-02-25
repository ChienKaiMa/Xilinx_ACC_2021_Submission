# Xilinx ACC 2021 Submisson
EXTREME TRADING SOLUTION: Quantum-accelerated trading strategies on Accelerated Algorithmic Trading (AAT) Framework

## 1-1 Project Abstraction
Quantum Bifurcation Machines can be used for quantum adiabatic optimization and universal quantum computation. TOSHIBA has realized Quantum Bifurcation Machines to Simulated Bifurcation Machine（SBM）Technologies accelerated with NVIDIA GPU.
We design and implement Quantum-accelerated Trading Strategies for currency exchange with replaceable algorithms modular（e.g. Simulated Bifurcation, SB or Simulated Quantum Annealing, SQA）on Xilinx Accelerated Algorithmic Trading (AAT) framework, which is a Fully featured open source reference design for trading applications.

## 1-2 Project Data Format
by Justin

## 1-3 Source Compiling
Development Environment
* A x86 server installed with a Xilinx Avelon U50 accelrator
* A x86 server installed with a Broadcom BCM957711A 10Gb x 2 SFP port card
* QSFPx1-to-SFPx4 cable
* Xilinx Accelerated Algorithmic Trading reference package Q2 (UG1067 v1.1 July 2, 2021)
* Operation system: Ubuntu 20.04.2 LTS

Settings in ~/.bashrc:

    source /opt/Xilinx/Vitis/2021.1/settings64.sh
    source /opt/xilinx/xrt/setup.sh
    export PLATFORM_REPO_PATHS='/opt/xilinx/platforms'
    export LM_LICENSE_FILE="~/Xilinx.lic"
    export XILINX_PLATFORM='xilinx_u50_gen3x16_xdma_201920_3'
    export DEVICE=${PLATFORM_REPO_PATHS}/${XILINX_PLATFORM}/${XILINX_PLATFORM}.xpfm
    export DM_MODE=DMA
    
 Compiling instructions:

    $ cd ../Accelerated_Algorithmic_Trading/build
    $ make clean
    $ ./buildall.sh
    
## 1-4 Test Flow

## 2-1 Modeling

## 2-2 SQA Design & Implementation

## 2-3 SBM Design & Implementation

## 3-1 HLS Benefit

## 3-2 AAT Framework Benefit

