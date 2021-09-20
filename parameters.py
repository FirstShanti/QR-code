import argparse
from datetime import datetime


def get_params():

	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-t',
        '--text',
        required=False,
		help='text to decode in QR code'
	)
	parser.add_argument(
		'-f',
		'--file',
		required=False,
		help='path to file with text to decode in QR code',
	)
	args = vars(parser.parse_args())
	return args