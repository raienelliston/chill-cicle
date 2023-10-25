import cv2

class qrCode:
    def __init__(self, device = 0):
        self.device = device
        self.camera = cv2.VideoCapture(self.device)
        self.qrCode = cv2.QRCodeDetector()

    def read(self):
        return self.data

    def show(self):
        _, frame = self.camera.read()
        data, bbox, _ = self.qrCode.detectAndDecode(frame)
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color = (255, 0, 0), thickness = 2)
            cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.imshow("QR Code", frame)
            cv2.waitKey(1)
        if data:
            self.data = data

    def device(self):
        return self.device

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import os
    qrCode = qrCode()
    while True:
        qrCode.show()
        print(qrCode.read())