import argparse
import pathlib
import math
from PIL import Image
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('xml', help='The path of the XML file.')
parser.add_argument('img', help='The path of the image file.')
parser.add_argument('-d', '--downsize', help='Image downsizing factor.', default = 2)
parser.add_argument('-s', '--saveframes', help='Save frames flag.', action = "store_true")
args = parser.parse_args()

downsize = int(args.downsize)
saveframes = bool(args.saveframes)

if (downsize % 2 != 0 or downsize == 0):
    raise ValueError("Downsizing factor should be a multiple of 2 for Integer Scaling.")

xmlPath = pathlib.Path() / args.xml
imgPath = pathlib.Path() / args.img
tree = ET.parse(xmlPath)
root = tree.getroot()

newImage = Image.open(imgPath)
width, height = newImage.size

# resample=0 for nearest neighbour, 1 for lanczos, 2 bilinear, 3 cubic, 4 box, 5 hamming
newImage = newImage.resize((int(width/downsize), int(height/downsize)), resample=2)
newImage.save(imgPath)

def scale(value):
    return str(math.floor(int(value)/downsize))

for subtext in root.findall('SubTexture'):
    subtext.set('x', scale(subtext.get('x')))
    subtext.set('y', scale(subtext.get('y')))
    subtext.set('width', scale(subtext.get('width')))
    subtext.set('height', scale(subtext.get('height')))

    if (saveframes):
        if (subtext.get('frameWidth') is not None):
            subtext.set('frameWidth', subtext.get('frameWidth'))

        if (subtext.get('frameHeight') is not None):
            subtext.set('frameHeight', subtext.get('frameHeight'))

        if (subtext.get('frameX') is not None):
            subtext.set('frameX', subtext.get('frameX'))

        if (subtext.get('frameY') is not None):
            subtext.set('frameY', subtext.get('frameY'))
    else:
        if (subtext.get('frameWidth') is not None):
            subtext.set('frameWidth', scale(subtext.get('frameWidth')))

        if (subtext.get('frameHeight') is not None):
            subtext.set('frameHeight', scale(subtext.get('frameHeight')))
        
        if (subtext.get('frameX') is not None):
            subtext.set('frameX', scale(subtext.get('frameX')))

        if (subtext.get('frameY') is not None):
            subtext.set('frameY', scale(subtext.get('frameY')))

tree.write(xmlPath, encoding='utf-8', xml_declaration=True)