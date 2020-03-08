# Project Title

This project focus on wellbeing of gamers and anyone who considers a bit seriousness in gaming. It uses gaming webcam to collect information regarding your mental state. It helps to give you an approx. idea of how your state of mind after a gaming session. Now whats the importance. Well ofcourse its important to get an idea of your mental state as it shows your health too. Gaming rage can be a serious issue if not controlled<br>

This project is build on Intel Openvino Toolkit as its a very good technology for edge application and inference making on edge. And GWELL stands for Gamers Well-Being ;)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Intel Openvino
VS Studio 15>
CMake
Python
```

### Installing

To get the project in your local machine

```
git clone https://github.com/akhilmhdh/GWELL.git
```

Now to setup the intel openvino global variables, this can also be automated too or added to your system global variable.

```
Go to _install_directory(default:C:\Program Files (x86))IntelSWTools\openvino\bin\
Run setupvars.bat in commandline
```

Then in same commandline

```
Go to project_directory
Run python main.py
```

Now the output after you end your session will be like this saved in data folder.

![Output Image](https://github.com/akhilmhdh/GWELL/blob/master/data/08-Mar-2020-16-07.png)

## Built With

- [Openvino](https://docs.openvinotoolkit.org/)
- [Python](https://www.python.org/doc/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Intel openvino
- Udacity
