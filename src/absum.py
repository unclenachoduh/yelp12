import sys

from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file("UncleNachoDuhTempFolder/temp", num_epochs=3)
textgen.generate()