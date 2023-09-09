"""
Brandon Bell
September 2023
Generate "Unicode Block" characters based on user input.
This is  just to make cool looking titles in structured text sections
of my PLC programs. I'm sure there's an easier (already existing) way
to do this, but it seemed like a fun challenge to make a program to
do this.
"""

# Unicode Character Index Reference
# █  Full Block {solid} = U+2588
# ╔  Box Drawings Double Down and Right = U+2554
# ╗  Box Drawings Double Down and Left  = U+2557
# ═  Box Drawings Double Horizontal     = U+2550
# ╚  Box Drawings Double Up and Right   = U+255A
# ╝  Box Drawings Double Up and Left    = U+255D
# ║  Box Drawings Double Vertical       = U+2551

fb = chr(0x2588)
dr = chr(0x2554)
dl = chr(0x2557)
hz = chr(0x2550)
ur = chr(0x255A)
ul = chr(0x255D)
vr = chr(0x2551)
sp = " "

selected = input("Input a word:\n").upper().replace(" ", "")

A = [[sp, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, fb, fb, fb, fb, fb, vr],
     [fb, fb, dr, hz, hz, fb, fb, vr],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [ur, hz, ul, sp, sp, ur, hz, ul]]

B = [[fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, fb, fb, fb, fb, dl, ul],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, fb, fb, fb, fb, dl, ul],
     [ur, hz, hz, hz, hz, hz, ul, sp]]

C = [[sp, fb, fb, fb, fb, fb, fb, dl],
     [fb, fb, dr, hz, hz, hz, hz, ul],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [ur, fb, fb, fb, fb, fb, fb, dl],
     [sp, ur, hz, hz, hz, hz, hz, ul]]

D = [[fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [fb, fb, fb, fb, fb, fb, dr, ul],
     [ur, hz, hz, hz, hz, hz, ul, sp]]

E = [[fb, fb, fb, fb, fb, fb, fb, dl],
     [fb, fb, dr, hz, hz, hz, hz, ul],
     [fb, fb, fb, fb, fb, dl, sp, sp],
     [fb, fb, dr, hz, hz, ul, sp, sp],
     [fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, hz, hz, hz, hz, ul]]

F = [[fb, fb, fb, fb, fb, fb, fb, dl],
     [fb, fb, dr, hz, hz, hz, hz, ul],
     [fb, fb, fb, fb, fb, dl, sp, sp],
     [fb, fb, dr, hz, hz, ul, sp, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [ur, hz, ul, sp, sp, sp, sp, sp]]

G = [[sp, fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, hz, hz, ul, sp],
     [fb, fb, vr, sp, sp, fb, fb, fb, dl],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [ur, fb, fb, fb, fb, fb, fb, dr, ul],
     [sp, ur, hz, hz, hz, hz, hz, ul, sp]]

H = [[fb, fb, dl, sp, sp, fb, fb, dl],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [fb, fb, fb, fb, fb, fb, fb, vr],
     [fb, fb, dr, hz, hz, fb, fb, vr],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [ur, hz, ul, sp, sp, ur, hz, ul]]

I = [[fb, fb, dl],
     [fb, fb, vr],
     [fb, fb, vr],
     [fb, fb, vr],
     [fb, fb, vr],
     [ur, hz, ul]]

J = [[sp, sp, sp, sp, sp, fb, fb, dl],
     [sp, sp, sp, sp, sp, fb, fb, vr],
     [sp, sp, sp, sp, sp, fb, fb, vr],
     [fb, fb, dl, sp, sp, fb, fb, vr],
     [ur, fb, fb, fb, fb, fb, dr, ul],
     [sp, ur, hz, hz, hz, hz, ul, sp]]

K = [[fb, fb, dl, sp, sp, fb, fb, dl],
     [fb, fb, vr, sp, fb, fb, dr, ul],
     [fb, fb, fb, fb, fb, dr, ul, sp],
     [fb, fb, dr, hz, fb, fb, dl, sp],
     [fb, fb, vr, sp, ur, fb, fb, dl],
     [ur, hz, ul, sp, sp, ur, hz, ul]]

L = [[fb, fb, dl, sp, sp, sp, sp, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, hz, hz, hz, hz, ul]]

M = [[fb, fb, fb, dl, sp, sp, sp, fb, fb, fb, dl],
     [fb, fb, fb, fb, dl, sp, fb, fb, fb, fb, vr],
     [fb, fb, dr, fb, fb, fb, fb, dr, fb, fb, vr],
     [fb, fb, vr, ur, fb, fb, dr, ul, fb, fb, vr],
     [fb, fb, vr, sp, ur, hz, ul, sp, fb, fb, vr],
     [ur, hz, ul, sp, sp, sp, sp, sp, ur, hz, ul]]

N = [[fb, fb, fb, dl, sp, sp, sp, fb, fb, dl],
     [fb, fb, fb, fb, dl, sp, sp, fb, fb, vr],
     [fb, fb, dr, fb, fb, dl, sp, fb, fb, vr],
     [fb, fb, vr, ur, fb, fb, dl, fb, fb, vr],
     [fb, fb, vr, sp, ur, fb, fb, fb, fb, vr],
     [ur, hz, ul, sp, sp, ur, hz, hz, hz, ul]]

O = [[sp, fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, hz, fb, fb, dl],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [ur, fb, fb, fb, fb, fb, fb, dr, ul],
     [sp, ur, hz, hz, hz, hz, hz, ul, sp]]

P = [[fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, fb, fb, fb, fb, dr, ul],
     [fb, fb, dr, hz, hz, hz, ul, sp],
     [fb, fb, vr, sp, sp, sp, sp, sp],
     [ur, hz, ul, sp, sp, sp, sp, sp]]

Q = [[sp, fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, hz, fb, fb, dl],
     [fb, fb, vr, fb, sp, sp, fb, fb, vr],
     [ur, fb, fb, fb, fb, fb, fb, dr, ul],
     [sp, ur, hz, hz, hz, fb, dr, ul, sp],
     [sp, sp, sp, sp, sp, ur, ul, sp, sp]]

R = [[fb, fb, fb, fb, fb, fb, dl, sp],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, fb, fb, fb, fb, dr, ul],
     [fb, fb, dr, hz, hz, fb, fb, dl],
     [fb, fb, vr, sp, sp, fb, fb, vr],
     [ur, hz, ul, sp, sp, ur, hz, ul]]

S = [[fb, fb, fb, fb, fb, fb, fb, dl],
     [fb, fb, dr, hz, hz, hz, hz, ul],
     [fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, hz, hz, fb, fb, vr],
     [fb, fb, fb, fb, fb, fb, fb, vr],
     [ur, hz, hz, hz, hz, hz, hz, ul]]

T = [[fb, fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, fb, fb, dr, hz, hz, ul],
     [sp, sp, sp, fb, fb, vr, sp, sp, sp],
     [sp, sp, sp, fb, fb, vr, sp, sp, sp],
     [sp, sp, sp, fb, fb, vr, sp, sp, sp],
     [sp, sp, sp, ur, hz, ul, sp, sp, sp]]

U = [[fb, fb, dl, sp, sp, sp, fb, fb, dl],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [fb, fb, vr, sp, sp, sp, fb, fb, vr],
     [ur, fb, fb, fb, fb, fb, fb, dr, ul],
     [sp, ur, hz, hz, hz, hz, hz, ul, sp]]

V = [[fb, fb, dl, sp, sp, sp, sp, sp, fb, fb, dl],
     [ur, fb, fb, dl, sp, sp, sp, fb, fb, dr, ul],
     [sp, ur, fb, fb, dl, sp, fb, fb, dr, ul, sp],
     [sp, sp, ur, fb, fb, fb, fb, dr, ul, sp, sp],
     [sp, sp, sp, ur, fb, fb, dr, ul, sp, sp, sp],
     [sp, sp, sp, sp, ur, hz, ul, sp, sp, sp, sp]]

W = [[fb, fb, dl, sp, sp, sp, sp, sp, fb, fb, dl],
     [fb, fb, vr, sp, fb, fb, dl, sp, fb, fb, vr],
     [fb, fb, vr, fb, fb, fb, fb, dl, fb, fb, vr],
     [fb, fb, fb, fb, dr, hz, fb, fb, fb, fb, vr],
     [fb, fb, fb, dr, ul, sp, ur, fb, fb, fb, vr],
     [ur, hz, hz, ul, sp, sp, sp, ur, hz, hz, ul]]

X = [[fb, fb, dl, sp, sp, fb, fb, dl],
     [ur, fb, fb, dl, fb, fb, dr, ul],
     [sp, ur, fb, fb, fb, dr, ul, sp],
     [sp, fb, fb, dr, fb, fb, dl, sp],
     [fb, fb, dr, ul, ur, fb, fb, dl],
     [ur, hz, ul, sp, sp, ur, hz, ul]]

Y = [[fb, fb, dl, sp, sp, sp, fb, fb, dl],
     [ur, fb, fb, dl, sp, fb, fb, dr, ul],
     [sp, ur, fb, fb, fb, fb, dr, ul, sp],
     [sp, sp, ur, fb, fb, dr, ul, sp, sp],
     [sp, sp, sp, fb, fb, vr, sp, sp, sp],
     [sp, sp, sp, ur, hz, ul, sp, sp, sp]]

Z = [[fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, hz, fb, fb, fb, vr],
     [sp, fb, fb, fb, fb, fb, dr, ul],
     [fb, fb, fb, dr, hz, hz, ul, sp],
     [fb, fb, fb, fb, fb, fb, fb, dl],
     [ur, hz, hz, hz, hz, hz, hz, ul]]

letter_dictionary = {
    "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K, "L": L, "M": M,
    "N": N, "O": O, "P": P, "Q": Q, "R": R, "S": S, "T": T, "U": U, "V": V, "W": W, "X": X, "Y": Y, "Z": Z
}

output = []

for char in selected:
    output += letter_dictionary[char]

for char in output:
    print(*char)
