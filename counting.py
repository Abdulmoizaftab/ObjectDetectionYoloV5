from roboflow import Roboflow
import os, sys, re, glob

# obtaining your API key: https://docs.roboflow.com/rest-api#obtaining-your-api-key
rf = Roboflow(api_key="1jGy96t0jtVCaw3vnKZi")
workspace = rf.workspace("14")
project = rf.workspace("14").project("mask-wearing")
# replace REPLACE_WITH_MODEL_VERSION_NUM with your model version number
version = project.version(14)
model = version.model

def count_object_occurances(predictions, target_class):
  """
    Helper method to count the number of objects in an image for a given class
    :param predictions: predictions returned from calling the predict method
    :param target_class: str, target class for object count
    :return: dictionary with target class and total count of occurrences in image
  """
  object_counts = {target_class : 0}
  for prediction in predictions:
    if prediction['class'] in target_class:
      object_counts[prediction['class']] += 1
  return object_counts



# perform inference on the selected image
# predictions = model.predict("pistol2.jpg") # or
## uncomment the following line to run inference on a hosted image
# predictions = model.predict("rtsp://admin:Admin@123@192.168.1.111/cam/realmonitor?channel=1subtype=1", hosted=True)

import cv2
cap = cv2.VideoCapture("rtsp://admin:Admin@123@192.168.1.111/cam/realmonitor?channel=1subtype=1")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    predictions = model.predict(frame)
    class_counts = count_object_occurances(predictions,'mask')
    print(frame, class_counts)
    print('\n')
cap.release()
cv2.destroyAllWindows()

## replace target_class with name of target_class
## example, target class is 'face': count_object_occurances(predictions, 'face')
