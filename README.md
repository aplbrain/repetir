# **repetir**
> A tool to easily reproduce big-data processing workflows using docker.

## Overview 

`repetir` allows you to quickly reproduce experimental results from published data and compare the results to your personal data all within a dockarized environment. 

<img src="https://github.com/aplbrain/repetir/blob/master/images/docker1.png" width="450" height="300" align="right"/>

Thus far the tool works as a repository hub that fascilitates the use of data processing workflows by composing a set of docker containers that include: a DVID instance in which pre-selected data is loaded into, and a python script or exposed Jupyter notebook in which the workflow lives, and which can immidiatey communicate with the DVID instance. 

Addtionally, `repetir` allows you to use [intern](https://github.com/jhuapl-boss/intern) to upload data from within the jupyter notebook to your existing instance of DVID. This fasciliates result comparison between the pre-selected published data set and your personal data.  
> Information on how to use the `intern` SDK can be found [here](https://github.com/jhuapl-boss/intern). `intern` (Integrated Toolkit for Extensible and Reproducible Neuroscience) is a Python 2/3 module that enables big-data neuroscience. 

## repetir xbrain <img src="https://github.com/aplbrain/repetir/blob/master/images/docker2.png" width="200" height="100" align="right"/>

This tool allows an [xbrain](http://luisrodriguezeng.com/) user to quickly spin up a DVID instance with pre-loaded public data and a dockerized jupyter-notebook containing the xbrain code pre-formatted to accomodated the pre-loaded DVID data. 

Seeing as this tool is still not an SDK we require the user clone this repository onto their computer and use the tools in the following way:

1. Clone this repository (https://github.com/aplbrain/repetir.git)

2. Make sure to change into the `xbrain` workflow directory and edit the docker-compose.yml file by changing the mounted volume to whatever you desire. 
>You can change it to a website which allows you to pull data from Google Drive or Google Cloud storage service or simply a local directory where you can find your data. 
>You may actually change this as many times as you want, and the program will just spin up the same dvid instance, keep the old uploaded data and load the new set as well. 

3. Allow docker to run two docker containers, the DVID instance and the xbrain workflow and connect them to each other. The command below will also change the values inside the xbrain workflow Jupyter Notebook to import the data you pre-selected, using `intern`. Run the following command from your shell:
```
docker-compose up
```

4. Start the right DVID instance with your pre-selected data. Run this last command from your shell (Run this only once):
```
python3 xBrainStart.py
```
  NOTE: If you want to shut down your container and bring them back on you are free to do so, all your data will be saved     inside the DVID instance, you WILL NOT have to run the command (4) again.
 
If you choose to upload your own data onto the running DVID instance you can do so by simply creating a new notebook on the xbrain instance and uploading your data using the instructions found on the [intern](https://github.com/jhuapl-boss/intern/wiki/DVID-Upload-Cutout-Tutorial-(RemoteExtension-Branch)) repository.

A summary of the steps to use this service is found below:

1. `git clone https://github.com/aplbrain/repetir.git`
2. `cd repetir && cd xbrain`
3. `docker-compose up`
4. `python3 xbrainStart.py`

We hope to simplify the steps above in the near future by publishing repetir as an SDK that allows the user to simply state `repetir xbrain brain2` where `xbrain` refers to the workflow and `brain2` refers to the data set to be processed. Our team is currently working on this feature.

NOTE: You may shut off all your containers when you wish to do so and the data will still be inside the DVID instance when you run `docker-compose up` again. 

## repetir's future
We hope to expand this tool to communicate with other public data processing workflows and makes it easier for users to reproduce and compare thier computational scientific results. 
