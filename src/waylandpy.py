import subprocess
import os

if os.getenv('XDG_SESSION_TYPE') != "wayland":
	raise Exception('This library only works on wayland')

class Wayland:
	def __init__(self):
		result = subprocess.run(["wayland-info"],text=True,capture_output=True)
		self.current_desktop = os.getenv('XDG_CURRENT_DESKTOP').lower()
		if result.returncode == 0:
			info = result.stdout
			self.width = info.split('logical_width: ')[1].split(",")[0]
			self.height = info.split('logical_height: ')[1].split("\n")[0]
		else:
			self.width = self.height = 0

	def copy(self,text: str) -> bool:
		result = subprocess.run(['wl-copy',str(text)])
		if result.returncode == 0:
			return True
		return False

	def paste(self) -> str:
		result = subprocess.run(["wl-paste"],text=True,capture_output=True)
		if result.returncode == 0:
			return result.stdout
		return ""

	def write(self,text: str) -> None: # If this function not work, run this command 'sudo chmod 666 /dev/uinput'
		result = subprocess.run(["ydotool","type",str(text)],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		return None

	def moveTo(self,x: int,y: int) -> bool:
		if x < 0 or y < 0:
			return False
		if x > self.width or y > self.height:
			return False
		result = subprocess.run(["ydotool","mousemove",str(x),str(y)],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if result.returncode == 0:
			return True
		return False

	def press(self,key: str) -> bool: # You can use combinations like alt+f4, ctrl+alt+tab, super(or meta)+r
		result = subprocess.run(["ydotool","key",key],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if result.returncode == 0:
			return True
		return False
	
	def screenshot(self,path: str) -> bool:
		if self.current_desktop == "gnome":
			command = ["gnome-screenshot","-f",path]
		elif self.current_desktop == "kde":
			command = ["spectacle","-n","-f",path]
		else:
			command = ["grim",path]
		result = subprocess.run(command,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if result.returncode == 0:
			return True
		return False
