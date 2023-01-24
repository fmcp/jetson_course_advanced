# Advanced Getting Started with AI on Jetson Nano: Jetson Samples

These examples have been developed for the course "Getting Started with AI on Jetson Nano", taught by Francisco M. Castro with the collaboration of NVIDIA.


## How to use

Clone this repository with git and upload notebooks to your Google Drive:

```
git clone https://github.com/fmcp/jetson_course_advanced
```

Maybe neccesary:
```
sudo pip3 install --global-option=build_ext --global-option="-I/usr/local/cuda/include" --global-option="-L/usr/local/cuda/lib64" pycuda
```

Or copy this colabs in your Google Drive:
* TF to ONNX: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pzpTxNZNwimL2gIFnfoVWvAcQh133Za-)
* Pruning with Keras: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NR2A9wPjHIQJPaE0SgNXnq-Ntg7jjnP3)
* L1 pruning: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10btzzCDsNZpshVYAPokwMUzA03Zdtr5I)
* TF to ONNX Load example: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-HN6F5ItNOJDIKbX8yFtEHvY-nNZa8yi)

* Example1: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1O60VH-dH2JrTpcKJh9LCqdxsq2RVlgcv)
* Example2: [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q8M0Kw-Ub9xBOUuNAHIwWlGRVOUPXqT0)

## Proposed projects
* Identification of bottles with different drinks
* Identification of playing card suits
* Recognition of handwritten music notes
* Counting people in a room
* Facial emotion recognition

## Network routing for Linux Hosts
1. Connect your Jetson Nano to your computer using the Micro-USB cable.
2. Open your Network Manager and check if the wired connection is restricted to enp60s0
3. Enable IP forwarding echo 1 > /proc/sys/net/ipv4/ip_forward
4. Add the following routing rule for iptables: sudo iptables -t nat -A POSTROUTING -o XXX -j SNAT --to YYY where XXX is the interface used for your internet connection and YYY is the IP assigned to your computer. For example, for Wifi connections: iptables -t nat -A POSTROUTING -o wlo0 -j SNAT --to 172.18.14.155
5. Connect to the Jetson Nano: ssh nano@192.168.55.1

## Authors

* **Francisco M. Castro** - [fmcp](https://github.com/fmcp) (fcastro@uma.es) [<img alt="alt_text" width="15px" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" />](https://www.linkedin.com/in/francisco-manuel-castro-pay%C3%A1n-5099248b/)
* **Paula Ruíz Barroso** - [PaulaRuizB](https://github.com/PaulaRuizB) (pruizb@uma.es) [<img alt="alt_text" width="15px" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" />](https://www.linkedin.com/in/paula-ruiz-barroso/)

![logo](./img/logos.jpg)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
 
