#import mido
#import random
#import sys
#import time
import argparse

parser = argparse.ArgumentParser(description='Play an aleatoric.')
parser.add_argument('--root', dest='root', type = int, default=48,
                    help='root note of scale (default: 48)')
parser.add_argument('--beats', dest='beats', type = int, default=8,
                    help='Time signature of SIG beats per measure (default: 8)')
parser.add_argument('--bpm', dest='bmp', type = float, default="90.0",
                    help='Beat frequency of beats per minute (default: 90)')
parser.add_argument('--ramp', dest='ramp', type = float, default=0.5,
                    help='Fraction of the beat time for the note envelope (default: 0.5)')
parser.add_argument('--accent', dest='accent', type = float, default=5.0,
                    help='Volume for the first accent beat of each measure (default: 5.0)')
parser.add_argument('--volume', dest='volume', type = float, default=8.0,
                    help='Volume for the unaccented beats of each measure (default: 8.0)')
args = parser.parse_args()

print(args.root)