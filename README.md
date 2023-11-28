# Ark_imav23

## Introdutiton
This brach contains code for Perception Tasks:
- [x] Lane Tracking
- [x] QR Pose Estimation for landing
- [ ] SLAM

Here's the progress:
| [![Watch the video](https://img.youtube.com/vi/b6T7o22q-kY/hqdefault.jpg)](https://www.youtube.com/embed/b6T7o22q-kY) | [![Watch the video](https://img.youtube.com/vi/1KxsDlQUzjg/hqdefault.jpg)](https://www.youtube.com/embed/1KxsDlQUzjg) |
|:--:|:--:| 
| *Lane Tracking* | *QR Detection* |

## Pre Requisites
Add `rotorS` and `mav comm` repositories in the src.
```bash
git clone https://github.com/ethz-asl/rotors_simulator.git
git clone https://github.com/ethz-asl/mav_comm.git
```

Install `zbar`(for QR code, not required for Aruco)
```bash
sudo apt-get install libzbar0
```
