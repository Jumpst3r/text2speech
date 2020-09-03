import argparse
import time
from googletrans import Translator
from gtts import gTTS 


trans = Translator()

parser = argparse.ArgumentParser()
parser.add_argument("--inputFile", type=str, required=True)
parser.add_argument("--outputFolder", type=str, required=True)
args = parser.parse_args()

basename = args.inputFile.split(".")[0]
ext = args.inputFile.split(".")[1]
  

with open(args.inputFile, 'r') as file:
    lines = file.readlines()

text = ""

for line in lines:
    text += line


l = trans.detect(text).lang
gttsobj = gTTS(text=text, slow=False, lang=str(l)) 

gttsobj.save(args.outputFolder + "output.mp3") 