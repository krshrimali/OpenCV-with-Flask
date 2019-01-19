import cv2
import sys

if(len(sys.argv) >= 2):
    edge_count = int(sys.argv[1])
    image_name = str(sys.argv[2])
    image_path = "static/" + str(image_name)
else:
    edge_count = 100
    image_path = "static/Kushashwa.jpg"
# read an image
print("Path: ", image_path)
img = cv2.imread(image_path, 1)
edge = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), edge_count, 200)

cv2.imwrite("static/edge.jpg", edge)