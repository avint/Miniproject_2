# encoder

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def encod():
    img = plt.imread("static/gray.tiff")
    ii = Image.fromarray(img)
    ii.save("static/gray.png")
    img = np.array(img)
    # plt.imshow(img)
    # plt.title("Original image")
    # plt.show()
    img = img.reshape(256 * 256,)

    ch = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        ".",
        " ",
    ]
    f = open("static\data.txt", "r")
    m = f.read()
    print(m)
    e = ""
    m = m.replace(",", "0...0")
    m = m.replace("?", "0. .0")
    m = m.replace(":", "0 ..0")
    m = m.replace("\n", "0  .0")
    m = m.replace("'", "0.. 0")
    m = m.replace("%", "0.  0")
    m = m.replace(";", "0 . 0")

    for i in m:
        a = ch.index(i)
        b = bin(a).replace("0b", "")
        x = 1000000 + int(b)
        y = str(x)
        e += y[1:]

    l = len(e)
    r = 256 * 256
    lsb = e + "0" * (r - l)

    for i in range(0, r):
        a = img[i]
        a = bin(a)
        a = a.replace("0b", "")
        a = str(int(a) + 100000000)
        a = a[1:8] + lsb[i]
        img[i] = int(a, 2)

    img = img.reshape(256, 256)
    enc = Image.fromarray(img)
    enc.save("static/enimg.tiff")
    enc.save("static/enimg.png")

    # plt.imshow(img)
    # plt.title("Encoded Image")
    # plt.show()
