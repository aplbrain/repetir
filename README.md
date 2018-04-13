# **repetir**
> A tool to easily reproduce big-data processing workflows using docker.

## Overview 

`repetir` allows you to quickly reproduce experimental results from published data and compare the results to your personal data all within a dockarized environment. Thus far the tool works as a repository hub that fascilitates the use of data processing workflows by composing a set of docker containers that include a DVID instance in which pre-selected data is loaded into and a python script or exposed Jupyter notebook in which the workflow lives, and which can immidiatey communicate with the DVID instance. 

Similarly `repetir` allows you to then use the [intern](https://github.com/jhuapl-boss/intern) SDK to upload data to your existing instance of DVID to run the same workflow with your personal data. 
> Information on how to use the `intern` SDK can be found [here](https://github.com/jhuapl-boss/intern). `intern` (Integrated Toolkit for Extensible and Reproducible Neuroscience) is a Python 2/3 module that enables big-data neuroscience. 

## repetir xbrain
This tool allows an [xbrain](http://luisrodriguezeng.com/). user to quickly spin up a DVID instance with pre-loaded public data and a dockerized jupyter-notebook containing the xbrain code pre-formatted to accomodated the pre-loaded DVID data. 




## repetir's future
We hope to expand this tool to communicate with other public data processing workflows and makes it easier for users to reproduce and compare thier computational scientific results. 
