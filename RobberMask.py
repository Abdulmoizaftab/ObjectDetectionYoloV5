# from roboflow import Roboflow
# rf = Roboflow(api_key="xt9rAzuObTBuzfkY1y0s")
# project = rf.workspace().project("video-r7asz")
# model = project.version(1).model




from roboflow import Roboflow
rf = Roboflow(api_key="wOakuvyV6yJhqFM3gXDs")
project = rf.workspace("dani-gpbtu").project("final-k6z7a")
model = project.version(1).model

image2="D:/Online/SelectedJPG/42855_1.jpg_480Wx480H.jpg"
image3 = "https://images.unsplash.com/photo-1570913149827-d2ac84ab3f9a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80";

# infer on a local image
print(model.predict('https://www.shutterstock.com/image-photo/red-apple-isolated-on-white-600w-1727544364.jpg',confidence=20,hosted=True, overlap=30,labels=True).json())

# visualize your prediction
# model.predict("waqas.mp4", confidence=40, overlap=30).save("prediction.mp4")

# infer on an image hosted elsewhere
# print(model.predict("mask.jpg", hosted=True, confidence=40, overlap=30).json())


# file="infer.sh"
# # ROBOFLOW_KEY=xxxxx file/[YOUR_DATASET]/[YOUR_VERSION] video_in.mp4 video_out.mov
# ROBOFLOW_KEY='1jGy96t0jtVCaw3vnKZi'
# print(ROBOFLOW_KEY)