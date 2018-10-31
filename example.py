"""
    File name: example.py
    Author: rameshpr
    Date: 10/29/18
"""
import cv2
import pyyolo

meta_filepath = "/home/rameshpr/Downloads/darknet_google_server/data/obj.data"
cfg_filepath = "/home/rameshpr/Downloads/darknet_google_server/cfg/yolo-lb.cfg"
weights_filepath = "/home/rameshpr/Downloads/darknet_google_server/backup/yolo-v3.weights"

image_filepath = './image.jpg'

meta = pyyolo.load_meta(meta_filepath)
net = pyyolo.load_net(cfg_filepath, weights_filepath, False)

im = cv2.imread(image_filepath)
yolo_img = pyyolo.array_to_image(im)
res = pyyolo.detect(net, meta, yolo_img)

for r in res:
    cv2.rectangle(im, r.bbox.get_point(pyyolo.BBox.Location.TOP_LEFT, is_int=True),
                  r.bbox.get_point(pyyolo.BBox.Location.BOTTOM_RIGHT, is_int=True), (0, 255, 0), 2)

cv2.imshow('Frame', im)
cv2.waitKey(0)
