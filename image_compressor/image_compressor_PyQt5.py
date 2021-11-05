import sys
import json
import os
import tinify 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QRectF, QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, 
							QListWidgetItem, QLabel, QLineEdit, 
							QPushButton, QSizePolicy,
							QAbstractItemView, QHBoxLayout, QVBoxLayout, 
							QLayout)


def compress_image(image_source, output_file_path):
	try:
		image_file_name = os.path.basename(image_source)
		source = tinify.from_file(image_source)
	except tinify.errors.AccountError:
		return (False, 'Invalid API Key')
	except tinify.errors.ConnectionError as e:
		return (False, str(e))
	except tinify.errors.ClientError:
		return (False, 'File type is not supported')
	else:
		source.to_file(output_file_path)
		return (True, 'Ok')




class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('TinyPNG Image Compressor')
		self.setWindowIcon(QIcon('1343439.ico'))
		self.window_width, self.window_height = 1800, 800
		self.setMinimumSize(self.window_width, self.window_height)
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.layoutRow1 = QHBoxLayout()
		self.layoutRow1.setSizeConstraint(QLayout.SetFixedSize)
		self.layout.addLayout(self.layoutRow1)
		labelPath = QLabel('&Export To: ')
		labelPath.setStyleSheet('font-size: 30px')
		self.layoutRow1.addWidget(labelPath)
		self.export_path = QLineEdit()
		self.export_path.setAlignment(Qt.AlignLeft)
		self.export_path.setMinimumHeight(50)
		self.export_path.setText(os.getcwd())
		self.layoutRow1.addWidget(self.export_path)
		labelPath.setBuddy(self.export_path)
		self.layoutRow2 = QHBoxLayout()
		self.layout.addLayout(self.layoutRow2)
		self.initColumnA()
		self.initColumnB()



	def initColumnA(self):
		layoutColumnA = QVBoxLayout()
		self.layoutRow2.addLayout(layoutColumnA, 8)
		self.listFiles = ImageListWidget()
		layoutColumnA.addWidget(self.listFiles)
		self.status = QLabel()
		layoutColumnA.addWidget(self.status)

	

	def initColumnB(self):
		layoutColumnB = QVBoxLayout()
		self.layoutRow2.addLayout(layoutColumnB)
		self.btnConvert = QPushButton('&Convert', clicked=self.compressImages)
		self.btnConvert.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.btnReset = QPushButton('&Reset', clicked=self.resetFields)
		self.btnReset.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.btnClose = QPushButton('C&lose', clicked=app.quit)
		self.btnClose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)       
		layoutColumnB.addWidget(self.btnConvert)
		layoutColumnB.addWidget(self.btnReset)
		layoutColumnB.addWidget(self.btnClose)
		layoutColumnB.addStretch()



	def compressImages(self):
		self.output_path = self.export_path.text()
		if not os.path.isdir(self.output_path):
			self.status.setText('Invalid Directory')
			return
		elif self.listFiles.count() == 0:
			self.status.setText('0 File')
			return
		self.worker = CompressImage(self)
		try:
			self.worker.finished.connect(self.threadFinished)
			self.worker.progress.connect(lambda v: self.status.setText('Prcessing {0}'.format(v)))
			self.worker.started.connect(self.threadStarted)
			self.worker.start()
		except Exception as e:
			self.status.setText(str(e))



	def threadStarted(self):
		self.btnConvert.setEnabled(False)
		self.btnReset.setEnabled(False)
		self.btnClose.setEnabled(False)
	


	def threadFinished(self):
		self.btnConvert.setEnabled(True)
		self.btnReset.setEnabled(True)
		self.btnClose.setEnabled(True)







class CompressImage(QThread):
	progress = pyqtSignal(str)
	
	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent



	def run(self):
		for i in range(self.parent.listFiles.count()-1, -1, -1):
			source_file = self.parent.listFiles.item(i).text()
			file_basename = os.path.basename(source_file)
			self.progress.emit(file_basename)
			
			response = compress_image(source_file, os.path.join(self.parent.output_path, file_basename))
			if response[1] != 'Ok':
				self.parent.status.setText(response[1])
				self.terminate()
			
			else:
				self.parent.listFiles.model().removeRow(i)








class ImageListWidget(QListWidget):
	def __init__(self, parent=None):
		super().__init__(parent=None)
		self.setStyleSheet('font-size: 30px;')
		self.setAcceptDrops(True)
		self.setDragDropMode(QAbstractItemView.InternalMove)
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)



	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			return super().dragEnter(event)
	


	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.accept()
		else:
			return super().dragMoveEvent(event)




	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.accept()
			images = []
			for url in event.mimeData().urls():
				if url.isLocalFile():
					if url.toString().endswith(('.jpeg', '.jpg', '.png')):
						images.append(str(url.toLocalFile()))
			self.addItems(images)
		else:
			super().dropEvent(event)





if __name__ == '__main__':
	api_key = json.load(open('api_key.json'))
	tinify.key = api_key['key']
	app = QApplication(sys.argv)
	app.setStyle('fusion')
	app.setStyleSheet('''
		QWidget {
			font-size: 30px;
			background-color: #3F3F5E
		}
		QPushButton {
			width: 240px;
			height: 60px;
			background-color: #565880;
			color: #FFFFFF;
			border-radius: 10px;
		}
		QListWidget {
			background-color: #FFFFFF;
		}
		QLabel {
			color: #FFFFFF;
		}
		QLineEdit {
			background-color: #FFFFFF;
		}
	''')
	
	myApp = MyApp()
	myApp.show()
	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')
