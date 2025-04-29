## How to use?

### Import the library
```python
from waylandpy import Wayland # Import Wayland class
wl = Wayland()
```

### Copy a text
```python
wl.copy('Wayland is a display manager') # Copy text
```

### Get last copied text
```python
wl.paste() # Returns the last copied text
```

### Get screen size
```python
wl.width # returns width of monitor
wl.height # return height of monitor
```
### Move the mouse
```python
wl.moveTo(200,350) # Move mouse to X:200 and Y:350
```
### Write something
```python
wl.write('Python is a great language!') # writes text
```

### Simulate keyboard keys
> You can also write text and single character, but we recommend using the **write** function.

```python
wl.press('alt+f4') # Shut down window
wl.press('backspace') # delete a character
wl.press('b') # write one character 
```

```python
wl.screenshot('~/Desktop/new_screenshot') # Take a screenshot
```
## Mouse click
```python
wl.click(1) # Left click
wl.click(2) # Right click
wl.click(3) # middle click
```
# Some necessary tools
> waylandpy uses wayland-info and ydotool tools to work. You can install it with your distribution's package manager.

```bash
sudo apt install ytdotools wayland-info # For Debian/Ubuntu based distributions
sudo pacman -S ytdotools wayland-info # For Arch and Arch based distributions
sudo zypper install ytdotools wayland-info # For OpenSUSE
sudo dnf install ytdotools wayland-info # For Fedora
```



## Some possible challenges during development
> Wayland being a more secure display manager causes us some difficulties such as not being able to get the current location of the mouse or using tools such as ydotool, wayland-info etc. but I will try to overcome these problems soon.
