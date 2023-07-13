import cv2
import sys
import numpy


numpy.set_printoptions(threshold=sys.maxsize)
class QrScanner():
    def __init__(self, camNum = 0):
        self.cam = cv2.VideoCapture(camNum)
        self.detector = cv2.QRCodeDetector()
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]

    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def get_frame(self, show = True):
        _, frame = self.cam.read()

        # converting to gray-scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        data, points, _ = self.detector.detectAndDecode(gray)

        if points is not None:
            if data:
                for i in range(len(points)):
                    for j in range (len(points[i])):
                        start = j
                        end = j + 1
                        if end >= 4:
                            end = 0
                        cv2.line(frame, tuple([int(coor) for coor in points[i][start]]), tuple([int(coor) for coor in points[i][end]]), color=(255, 0, 0), thickness=2)
                    cv2.putText(frame, data, tuple([int(coor) for coor in points[i][2]]), cv2.FONT_HERSHEY_SIMPLEX, 1, (198, 76, 255), 2, cv2.LINE_AA)

                # print("[+] QR Code detected, data:", data)

        frame = cv2.resize(frame, (256,256))
        if show:
            cv2.imshow('video', frame)

        key = cv2.waitKey(1)
        _, jpeg = cv2.imencode('.jpg', frame, self.encode_param)
        return jpeg.tobytes(), data, frame


if __name__ == "__main__":
    cam = QrScanner(0)
    while True:
        jpegbytes, data, frame = cam.get_frame()
        # list_str = ",".join(map(str, jpeg))
        # list_int = list_str.split(',')
        # list_int = list(map(int, list_int))
        # print("Result: " + str(len(list_int)))
