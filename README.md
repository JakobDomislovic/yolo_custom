# YOLOv8 with custom dataset and configuration

YOLOv8 is a deep learning model developed by Ultralytics. More about YOLOv8 and Ultralytics can be found [here](https://github.com/ultralytics/ultralytics).

## Dataset
All about preparing the YOLOv8 dataset and what it should look like can be found [here](https://docs.ultralytics.com/datasets/detect/).

**N.B.** Proper preparation of the dataset is one of the most important parts for successful model learning! You should not skip it out and always check if your dataset meets the YOLOv8 conditions!

## Custom configuration

There is a defualt configuration (defualt.yaml) in this repository that you should use as an example. Each argument in default.yaml is described [here] (https://docs.ultralytics.com/usage/cfg/).

I suggest that you create a custom configuration file that suits your needs.

## Training, validation, prediction, ...
All this can be set in the configuration file in the `mode` argument. After training, all used arguments, diagrams, results and weights are saved in the ./`project`/`name` directory.

## TODO
- add tensorboard or clearML