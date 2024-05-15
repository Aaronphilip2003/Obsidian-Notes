 
Flowchart:
[[S-AES_Flowchart.excalidraw]]


16 bit plain text 
P (plaintext) = D7 28
Binary = 1101 0111 0010 1000

16 bit key = 4AF5
Binary = 0100 1010 1111 0101

### Constant Values
Rcon(1)= 10000000
Rcon(2)= 00110000
RotNib = Swap the nibbles (4 bit nibbles)
SubNib = Refer to the table below

S-Box Table

| 00  | 00  | 01  | 10  | 11  |
| --- | --- | --- | --- | --- |
| 00  | 9   | 4   | A   | B   |
| 01  | D   | 1   | 8   | 5   |
| 10  | 6   | 2   | 0   | 3   |
| 11  | C   | E   | F   | 7   |
 

```
w0 = first 8 bits of 16 bit key
w1 = next 8 bits of 16 bit key
w2 = w0 ⊕ Rcon(1) ⊕ Subnib(RotNib(w1))
w3 = w2 ⊕ w1
w4 = w2 ⊕ Rcon(2) ⊕ SubNib(RotNib(w3))
w5 = w4 ⊕ w3
key0 = w0w1
key1 = w2w3
key2 = w4w5

Lets assume you have a plaintext P 


Encryption:
Round 1

R0= key0 ⊕ P
Nibble Substitution= SubNib(R0) (Refer to S-box)
Shift Row (Swap 2nd and 4th nibble)
Mix Col Step =  [[1,4],[4,1]] X Shiftrow 
Use table for getting the multiplication values
convert the matrix to binary
then XoR
write them linearly
Add Round key 
linear ⊕ key1

Round 2
Subnib(0010 1011 0001 1011) - refer to sbox
shift row (swap 2 and 4 nibble) = sh (call it sh)
sh ⊕ key2
= answer (16bit cipher text)




```

### SOLUTION:

```
w0 = 0100 1010
w1 = 1111 0101
w2 = 1101 1101
w3 = 0010 1000
w4 = 1010 0111
w5 = 1001 1111
key0 = 01001010 11110101
key1 = 1101 1101 0010 1000
key2 = 1011 0111 1001 1111

Round 1

R0 = 1001 1101 1101 1101
Subnib(R0) = 0010 1110 1110 1110
ShiftRow = 0010 1110 1110 1110
[[1,4],[4,1]] X [0010 1110 1110 1110]
[[1,4],[4,1]] X [[2,E],[E,E]] = instead of adding XoR
eg) 1*2 ⊕ 4*E     4*2 ⊕ 1*E
    E*1 ⊕ 4*E     4*E ⊕ 1*E 
Now using table below 
2⊕D     8⊕E
E⊕D     D⊕E
convert to binary
0010 ⊕ 1101     0110 ⊕ 1110
1110 ⊕ 1101     1101 ⊕ 1110

Now XoR
1111    0110
0011    0011
write them linearly
1111 0110 0011 0011

add round key (linear ⊕ key1 )
1111 0110 0011 0011 ⊕ 11011101 00101000
= 0010 1011 0001 1011

Round 2

Subnib(0010 1011 0001 1011) - refer to sbox
= 1010 0011 0100 0011
Shiftow
= 1010 0011 0100 0011

(shiftrow ⊕ key2 )

1010 0011 0100 0011 ⊕ 1011 0111 1001 1111
=  answer
= 0001 0100 1110 1100
```

w2 = w0 ⊕ Rcon(1) ⊕ SubNib(RotNib(w1))
= 0100 1010 ⊕ 1000 0000 ⊕ SubNib(0101 1111)
= 1100 1010  ⊕ SubNib(0101 1111)
= 1100 1010 ⊕ 0001 0111
= 1101 1101

w3 = w2 ⊕ w1
= 1101 1101 ⊕ 1111 0101
= 0010 1000

w4 = w2 ⊕ Rcon(2) ⊕ SubNib(RotNib(w3))
= 1101 1101 ⊕ 0011 0000 ⊕ SubNib(1000 0010)
= 1110 1101 ⊕ Bin(6) Bin(A)
= 1110 1101 ⊕ 0110 1010
= 1011 0111

w5 = w4 ⊕ w3
= 1011 0111 ⊕ 0010 1000
= 1001 1111

key0 = 01001010 11110101
key1 = 11011101 00101000
key2 = 10100111 10011111

Encryption : 

R0 = key0⊕P

## Round 1

1) Nibble Substitution
SubNib(R0) (Refer to S-box) 
1001 1101 1101 1101 ------> 0010 1110 1110 1110

2) Shift Row (Swap 2nd and 4th nibble)
0010 1110 1110 1110

3) Mix column
| 1   | 4   |
| --  | --  |        -   constant matrix
| 4   |  1  |     


constant matrix X shiftrow ( hex values ) 
![[WhatsApp Image 2023-09-13 at 09.09.42.jpg]]


![[Pasted image 20230913095118.png]]


using table
 
2⊕D     E⊕D
8⊕E      D⊕E

Convert these to binary

0010 ⊕ 1101     1110 ⊕ 1101
0110 ⊕ 1110     1101 ⊕ 1110

After XoR

1111    0110        
0011    0011     

write them linearly

= 1111 0110 0011 0011

Add Round key
1111 0110 0011 0011  ⊕ key1 
1111 0110 0011 0011  ⊕ 1101 1101 0010 1000
0010 1011 0001 1011

Round 2
SubNib(0010 1011 0001 1011) = 1010 0011 0100 0011
Shift row = 1010 0011 0100 0011

1010 0011 0100 0011 ⊕ key2
1010 0011 0100 0011 ⊕ 1011 0111 1001 1111
0001 0100 1110 1100