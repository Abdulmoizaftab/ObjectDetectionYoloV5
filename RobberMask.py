from roboflow import Roboflow
rf = Roboflow(api_key="1jGy96t0jtVCaw3vnKZi")
project = rf.workspace().project("gunandmask")
model = project.version(2).model

# infer on a local image
# print(model.predict("mask.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("waqas.mp4", confidence=40, overlap=30).save("prediction.mp4")

# infer on an image hosted elsewhere
# print(model.predict("mask.jpg", hosted=True, confidence=40, overlap=30).json())


# file="infer.sh"
# # ROBOFLOW_KEY=xxxxx file/[YOUR_DATASET]/[YOUR_VERSION] video_in.mp4 video_out.mov
# ROBOFLOW_KEY='1jGy96t0jtVCaw3vnKZi'
# print(ROBOFLOW_KEY)