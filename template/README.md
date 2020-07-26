# Template for Contributed Dataset

## Overview

Use this directory as a template if you wish to contribute a dataset.
Each dataset is housed within a separate directory in [datasets](datasets/).
You will need to modify this README with the content described below
using [Markdown](https://guides.github.com/features/mastering-markdown/).
First, you should describe the dataset and how it might be used at a high-level.
We strongly encourage the use of freely available languages such R and Python for processing
and analysis of data.

## Description

Next, provide a detailed description of the data.
The original or otherwise unprocessed dataset.
If there are multiple versions, describe how they differ.
If your directory name is %dataset%, then the original dataset
should have the same name plus the appropriate file type extension
For example, *%dataset%.csv*.
Processed versions should be descriptively named
For example, *%dataset%-standardized.csv* or *%dataset%-cleaned.csv*.
Include any scripts used create the processed versions from the original.
Scripts should be prefixed with *generate-*, then the name of the dataset
that is output.
For example, *generate-%dataset%-standardized.R* or *generate-%dataset%-claned.R*.

## Example Analysis ##

You may optionally provide example analyses, including output numeric
and graphical results like the examples below.
Please include any scripts used to generate the results and use descriptive
names such as *%dataset%-linear-regression.R*.

Variable | Coefficient
---------|------------
intercept | 5.0
x | 0.15

![Example Figure](example.png)

*Wikimedia Commons / Public Domain*



## Sources and Licenses

Provide sources of all data.
If necessary, specify the license(s) for the data and scripts.
