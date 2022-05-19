import sys
import socket
import threading

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, lenght = 16, show = True):
        if isinstance(src, bytes):
            src = src.decode()

        results = list()
        for i in range(0, len(src), lenght):
            word = str(src[i:i+lenght])

            printable = word.translate(HEX_FILTER)
            hexa = ''.join([f'{ord(c):02X}' for c in word])
            hexwidth = lenght*3
            results.append(f'{i:04x}  {hexa:<{hexwidth}} {printable}')
        if show:
            for line in results:
                print(line)
            else:
                return results