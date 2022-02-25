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
* Operation system: Ubuntu 20.04.2 LTS
* Xilinx Vitis Software Platform 2021.1
* Xilinx Accelerated Algorithmic Trading reference package Q2 (UG1067 v1.1 July 2, 2021)

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
The pricingEngine::pricingProcess function is modified by replacing the original strategies with ERM and SBM functions.  AAT-SBM uses a different problem formulation from AAT-SQA, which is generated in the corresponding ERM module.
The SBM module takes the following as inputs: the Ising matrix representing the problem (Q_Matrix), two initialized arrays for SBM iterations (x and y), the number of iterations for the algorithm (steps), and two algorithm constants (c0, dt).  The only output (best_spin) represents the final result of the algorithm.  The arguments (best_energy and best_step) are intended to be outputs, but unused for now.  Our implementation sets steps as 10.
![2-3_001](https://user-images.githubusercontent.com/11850122/155672089-54bc1229-ddb1-4df9-8fba-dfae7039f08c.png)

The original design of SBM reads the matrix and arrays from PCIe,  Since the input matrix is generated on chip and is a static variable, there is no need to request the data from DDR.
After the inputs are loaded, the algorithm starts.  One SBM_update function represents one iteration of the algorithm.  The loop of 10 times (corresponding to the input argument steps) of SBM_update is unrolled.
To apply the DATAFLOW pragma, we divide the SBM_update module to four functions: update_x, set_spin, update_y, and reset_x_y.  In the ERM module, the ARRAY_PARTITION pragma is applied to J, which is Q_Matrix in SBM, so x and y in the dataflow are also partitioned.  Most parts of the four functions are pipelined and pass arrays by hls::stream.

update_x:
![2-3_002](https://user-images.githubusercontent.com/11850122/155672459-6136ec59-73cc-483e-825f-c6e89fab52d4.png)

set_spin:
The sign function of the x array is precalculated in this function.

update_y:
![2-3_003](https://user-images.githubusercontent.com/11850122/155672657-3a677a5a-7145-4fb2-a899-1a3e91b6eaaa.png)

To accelerate the calculation of the sum part in update_y, the balance adder tree is implemented.  As there are 19 elements to add, the helper functions pad the array to 32 elements and perform parallel fadd.
![2-3_004](https://user-images.githubusercontent.com/11850122/155672836-22fbdf43-7f50-4867-9d14-14df9715dd52.png)

reset_x_y:
![2-3_005](https://user-images.githubusercontent.com/11850122/155673023-3bf5083a-d0c2-4a7f-9c3b-66c4d89facc8.png)


## 3-1 HLS Benefit

## 3-2 AAT Framework Benefit
