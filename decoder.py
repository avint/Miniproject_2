# decoder

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def decod():
    img = plt.imread("static/enimg.tiff")
    ii = Image.fromarray(img)
    ii.save("static/enimg.png")
    img = np.array(img)
    img = img.reshape(256 * 256*4,)

    data = ""
    for i in range(0, len(img)):
        a = img[i]
        a = bin(a)
        a = a.replace("0b", "")
        a = str(int(a) + 100000000)
        data = data + a[8]

    l = len(data) // 6
    p = 0
    m = ""
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
    for i in range(l):
        t = data[p : p + 6]
        p += 6
        i = int(t, 2)
        m += ch[i]

    m = m.replace("0 . 0", ";")
    m = m.replace("0.  0", "%")
    m = m.replace("0.. 0", "'")
    m = m.replace("0  .0", "\n")
    m = m.replace("0 ..0", ":")
    m = m.replace("0. .0", "?")
    m = m.replace("0...0", ",")

    till = m.index("AAA")

    print(m[0:till])
    return m[0:till]

