# xbox-controller-wrapper

A little program that I made un a couple of hours to map controller
inputs to the keyboard and mouse in Windows. No more functionality
is planned for this software. This softwared was made for python 3.6
and has not been tried in other python versions.

## Python Dependencies required
* inputs

## Running the program
Just run main.py

`> python main.py`

## Configuring the controller
To configure the controller you have to edit the conf.py file.
There are 2 variables that change the controller mapped inputs:

### buttons

Buttons is the variable that maps all the buttons in the controller
(not including triggers or the plus pad). This buttons include:

* A Button
* B Button
* X Button
* Y Button
* Start Button: The button to the right at the middle of the controller.
* Select Button: The button to the left at the middle of the controller.
* L1 Button: The upper button to the left at the back of the controller.
* R1 Button: The upper button to the right at the back of the controller.

### absolute
* L2 Trigger: The lower trigger to the left at the back of the controller.
* R2 Trigger: The lower trigger to the right at the back of the controller.
* Plus Pad: The pad with directions (up, down, left right) of the controller.
* Left Analog
* Right Analog

In conf.py its explained how to map the controller to the keyboard and mouse.
