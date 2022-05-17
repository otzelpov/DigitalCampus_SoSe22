# Documentation for instant ngp


## **Installation guide**

**Links**:
+ [Github/intant-ngp](https://github.com/NVlabs/instant-ngp)
+ [COLMAP](https://colmap.github.io/install.html)
+ [CMake](https://cmake.org/download/)

**Note**:
1. OptiX is optional and we haven't used/installed it, since we used nerf instead of sdf.
2. Python is optional but we installed it, since there are some really usefull scripts inside `instant-ngp/scripts`

<br>

### **GNU/Linux**

1. Follow these instructions to install [instant-ngp](https://github.com/colmap/colmap/issues/1420#issuecomment-1117388017).
2. Install [COLMAP](https://colmap.github.io/install.html).
    + make sure to install Ceres Solver before compiling COLMAP


### **Windows**

You can follow [this step by step guide](https://www.youtube.com/watch?v=kq9xlvz73Rg) created by byclouddump. He also created a [github repo](https://github.com/bycloudai/instant-ngp-Windows).

We haven't tested it on windows (yet), so we are not sure which errors to expect.

<br>

### **Tips and known issues**

**Latest CMake**

It's recommended to have the latest [CMake Version](https://cmake.org/download/) installed. You may want to try this, if you are experiencing any cmake issues.

**COLMAP package broken under Ubuntu (Debian)**

If you installed colmap via aptitude, you might/will face the issue, that some scripts in the instant ngp folder don't work correctly or some colmap error is thrown.

You can fix this by [compiling colmap](https://colmap.github.io/install.html) from source.

**CUDA not able to interact with the graphics card**

1. Install Cuda Toolkit

Check if the nvidia cuda toolkit is installed.

```bash
sudo apt install nvidia-cuda-toolkit
```

2. Disable Secure Boot

Jonathan experienced the issue after a BIOS update. In his case the BIOS setting "Secure Boot" was set to true.
If you face the same issue, please try to disable it and test it again.

**Libboost No suitable build variant has been found**

[Check this github issue](https://github.com/colmap/colmap/issues/1420#issuecomment-1117388017)

<hr>
