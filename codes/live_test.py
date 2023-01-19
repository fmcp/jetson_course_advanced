import argparse
import cv2
import os
import tensorflow as tf
import numpy as np
import time

LABELS = ["Banana", "Lemon", "Orange", "Strawberry"] # UPDATE ME!!!!

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction=0.2
graph = tf.Graph()
graph.as_default()
session = tf.compat.v1.Session(graph=graph, config=config)
session.as_default()

def live_test(model_path):
	model = tf.keras.models.load_model(model_path)
	cap = cv2.VideoCapture(0)
	live_data = True
	while (live_data):
		# Capture frame-by-frame
		ret, orig_frame = cap.read()
		frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2RGB)
		frame = cv2.resize(frame, (224, 224))
		frame = np.expand_dims(frame, axis=0)
		frame = frame/255.0
		# Predict
		start = time.time()
		results = model.predict(frame)
		fps = 1.0 / (time.time() - start)
		results = np.squeeze(results)
		predicted_label = np.argmax(results)
		score = results[predicted_label]

		# Display the resulting frame
		res = "{} ({:0.1f}%); FPS: {:d}".format(LABELS[predicted_label], score*100, int(fps))
		cv2.putText(orig_frame, res, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)
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
