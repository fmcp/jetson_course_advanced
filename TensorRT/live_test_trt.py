import argparse
import cv2
import os
import numpy as np
import time
import tensorrt as trt
from TensorRT import common

LABELS = ["Banana", "Lemon", "Orange", "Strawberry"]  # UPDATE ME!!!!

TRT_LOGGER = trt.Logger()


def get_engine(onnx_file_path, engine_file_path=""):
    """Attempts to load a serialized engine if available, otherwise builds a new TensorRT engine and saves it."""
    if os.path.exists(engine_file_path):
        # If a serialized engine exists, use it instead of building an engine.
        # print("Reading engine from file {}".format(engine_file_path))
        with open(engine_file_path, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
            return runtime.deserialize_cuda_engine(f.read())



def live_test(model_path):
    logos = cv2.imread("../../img/logos.jpg")

    # model = tf.keras.models.load_model(model_path)
    cap = cv2.VideoCapture(0)
    live_data = True
    with get_engine("no", model_path) as engine, engine.create_execution_context() as context:
        ret, orig_frame = cap.read()
        frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224))
        frame = np.expand_dims(frame, axis=0)
        frame = frame.astype(np.float16)
        print(frame.dtype)
        frame = frame / 255.0
        frame = frame.astype(np.float16)
        print(frame.dtype)
        # frame = frame.astype(float)
        inputs_trt, outputs_trt, bindings_trt, stream_trt = common.allocate_buffers(engine, frame)
        while (live_data):
            # Capture frame-by-frame
            ret, orig_frame = cap.read()
            frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224))
            frame = np.expand_dims(frame, axis=0)
            frame = frame.astype(np.float16)
            # print(frame.dtype)
            frame = frame / 255.0
            frame = frame.astype(np.float16)
            # print(frame.dtype)

            # Predict
            start = time.time()
            # results = model.predict(frame)

            # Do inference
            # Set host input to the image. The common.do_inference function will copy the input to the GPU before executing.
            inputs_trt[0].host = frame
            # inputs[0].host = np.abs(inputs[0].host)
            results = common.do_inference_v2(context, bindings=bindings_trt, inputs=inputs_trt,
                                             outputs=outputs_trt, stream=stream_trt)

            # print(results)
            fps = 1.0 / (time.time() - start)
            results = np.squeeze(results)
            predicted_label = np.argmax(results)
            score = results[predicted_label]

            # Display the resulting frame
            res = "{} ({:0.1f}%); FPS: {:d}".format(LABELS[predicted_label], score * 100, int(fps))
            cv2.putText(orig_frame, res, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)

            # Insert logos
            lw, lh, lc = logos.shape
            w, h, c = orig_frame.shape
            orig_frame[w - lw:, h - lh:, :] = logos
            orig_frame = cv2.resize(orig_frame, (1840, 1000))
            cv2.imshow('Prediction', orig_frame)
            pressedKey = cv2.waitKey(1) & 0xFF
            if pressedKey == ord('q'):
                live_data = False

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Input arguments
    parser = argparse.ArgumentParser(description='Test a CNN')
    parser.add_argument('--model_path', type=str, required=False, default="", help="Path to the trained model")

    args = parser.parse_args()
    model_path = args.model_path

    if os.path.exists(model_path):
        live_test(model_path)
    else:
        print("Wrong file_path!", model_path)