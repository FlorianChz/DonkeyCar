# DonkeyCar


The project has different requirements, the most important one is that the car must follow the track without hitting walls. There will be some obstacles on the track that the car needs to avoid, and one crosswalk where the car must break if there is a pedestrian and continue if there is not. Some traffic signs like stop sign or left and right direction arrows.

The track shape can’t change, as the location of the directional arrows but the obstacles and stop signs can be arranged everywhere.

The directional arrows are placed at the start of the track so that the car chooses a direction and thus a direction of circulation, i.e. to drive on the circuit in the clockwise or trigonometric direction.


To reduce the distortion, we have used the articles found [here](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) and [here](https://automaticaddison.com/how-to-perform-camera-calibration-using-opencv/). We then cropped the images to remove the unnecessary part of the images. 

images

We used the Keras linear model which is explained [here](https://medium.com/@paulux.bertin/autonomous-car-project-1f3dae08529c). There are also other models.

# Some advice

    -The quality of the data is paramount. Do not hesitate to collect data again if it is not good.  The quality of the model depends largely on the data. If the data is not good, the model will not be good either.  
	
    -The files that make up the donkey file are very numerous and long to read and understand but they are a real asset for understanding the functioning of the car. We started to read them too late, although they contained crucial information.
