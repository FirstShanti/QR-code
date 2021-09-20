import qrcode

from pathlib import Path
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styledpil import StyledPilImage

from parameters import get_params


class QR_GENERATOR():

	def __init__(self, argv):

		self.text = argv.get('text')
		self.file = argv.get('file')
		self.filepath = Path(self.file).expanduser() if self.file else None
		self.filename = self.filepath.name if self.filepath else None
		self.data = self.get_data()
		self.img = None


	def get_data(self):
		if self.text:
			return self.from_text()
		if self.file:
			return self.from_file()

	def from_text(self):
		return self.text

	def from_file(self):
		if self.filepath.is_file():
			return self.filepath.read_text()

	def generate(self):
		if self.data:
			qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
			qr.add_data(self.data)

			self.img = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())

			with open('qr.png', 'wb+') as f:
				self.img.save(f)
			self.img.show()


if __name__ == '__main__':
	parameters = get_params()
	qr = QR_GENERATOR(parameters)
	qr.generate()