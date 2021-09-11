# XMLSpriteResizer

Requirements:
````
 pip install Pillow
````
Usage:
````
 python xmlsr.py [args]
````

Args:
````
 -xml                  The path of the XML file.
 -img                  The path of the image file.
 -d                    Image downsizing factor. Default = 2.
 -sf, --saveframes     Save frames(frameXY and framesizes willn't be changed) flag. Default = False.
 -nb, --nobackup       Disable backuping flag.
````

Example:
````
 python xmlsr.py -img Hero.png -xml Hero.xml -nb
````
