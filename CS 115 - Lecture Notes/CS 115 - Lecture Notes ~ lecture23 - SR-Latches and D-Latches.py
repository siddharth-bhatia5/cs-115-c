# Sid Bhatia
# CS 115-C
# Lecture 23 - SR-Latches and D-Latches

# A 1-Bit Memory

## OR + NOT = NOR

### How do you store data using circuits?
### Circuits go only in one direction: e.g., North to South; West to East

### Loops in a circuit diagram = latch
### Results in the ability to remember values --> SR Latch
### Storage cicruit based on the latch

### Done using a NOR/NAND gate
### NOR:
###     x | y | x NOR y
###     ---------------------
###     0 | 0 |   1
###     0 | 1 |   0
###     1 | 0 |   0
###     1 | 1 |   0

### Take two NOR gates and take output
### Have the bottom wire be the complement of the top wire

### You don't want both S and R to be 1
### No matter what, if you have an input of 1 to a NOR gate, the output is 0

#### 1 --> NOR: 0 for \bar[Q]; therefore, 0 is fed into bottom NOR gate (see slide)
#### 0 and 0 --> NOR: 1 for Q since both inputs are 0

#### Therefore, if S = 1, then 1 in the top gate and 0 in the bottom gate, resulting in 1

#### If S = 0 --> NOR: 1 for \bar[Q] = 1; therefore 1 is fed into bottom NOR gate
#### 1 and 1 --> NOR: 0 for Q = 0

#### Both the cases of adding 0 and 1 is consistent with the 

#### *Set forces it to start 1 at top gate and 0 at bottom gate*; 
#### You remember what was the last one that was activated

#### If you change both S and R, it'll be in an inconsistent state; it'll stop oscilatting
#### but it'll be both 0 and its negation will be 0 at the same time (doesn't make sense)

# From S-R Latches to D-Latches

## To prevent changing from both S and R, you can implement a new circuit called D-Latch
### D AND Strobe --> top gate; ~D AND Strobe --> bottom gate

###    D | Strobe | S = (D AND Strobe) | R = (~D AND STR))
###    0 |   0    |         0          |        0
###    0 |   1    |         0          |        1
###    1 |   0    |         0          |        0
###    1 |   1    |         1          |        0

### S and R will never both be 1

### D-Latch allows you to express the bit you want to write and store it --> Data Bit
### More stable way of configuring memory
### When Strobe = 1, you're writing into memory; when Strobe = 0; you're not writing into memory

### Top bit is data bit

# Random Access Memory (RAM)

## You can bundle a bunch of D-Latches together to create a RAM

### 4 x 3 memory: 4 entries where each entry has 3 bits (number of entries = power of 2; entry has any # of bits)

### Bundle 3 D-Latches together by adding them together (have 6 data pins)