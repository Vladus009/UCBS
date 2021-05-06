all:
	pyinstaller main.py


clean:
	rm -rf build/ dist/ __pycache__/ *.spec


windows:
	pyinstaller main_windwos.py


linux:
	pyinstaller main.py


windows_onefile:
	pyinstaller --onefile main_windwos.py


linux_onefile:
	pyinstaller --onefile main.py
