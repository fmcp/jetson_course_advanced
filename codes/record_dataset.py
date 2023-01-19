import argparse
import cv2
import os
import glob

def get_last_counter(images_path):
	files_list = glob.glob(os.path.join(images_path, '*.png'))
	if len(files_list) == 0:
		return 0
	else:
		file_parts = files_list[-1].split('/')[-1].split('.')[0]
		return int(file_parts)

def collect_data(outdir, class_name):
	cap = cv2.VideoCapture(0)
	counter = get_last_counter(os.path.join(outdir, class_name))
	record_data = True
	while (record_data):
		# Capture frame-by-frame
		ret, frame = cap.read()

		# Display the resulting frame
		cv2.imshow('frame', frame)
		pressedKey = cv2.waitKey(1) & 0xFF
		if pressedKey == ord('s'):
			outpath = os.path.join(outdir, class_name, "{:09d}.png".format(counter))
			cv2.imwrite(outpath, frame)
			counter = counter + 1
		elif pressedKey == ord('q'):
			record_data = False

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	# Input arguments
	parser = argparse.ArgumentParser(description='Collects data for a class. For each class of the dataset, you must ejecute this code indicating the name of the label. If you push key s, it saves an image. q stop the recorcing')
	parser.add_argument('--outdir', type=str, required=False, default="", help="Output folder")
	parser.add_argument('--class_name', type=str, required=False, default="", help="Class name")

	args = parser.parse_args()
	outdir = args.outdir
	class_name = args.class_name

	if not os.path.exists(outdir):
		os.makedirs(outdir)

	if not os.path.exists(os.path.join(outdir, class_name)):
		os.makedirs(os.path.join(outdir, class_name))

	collect_data(outdir, class_name)
