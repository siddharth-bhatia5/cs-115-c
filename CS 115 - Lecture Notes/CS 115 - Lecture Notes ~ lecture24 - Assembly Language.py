# Sid Bhatia
# CS 115-C
# Lecture # - Assembly Language

# Workshop

## Write an assembly-langguage program that reads one integer, X,
## as keyboard input into register r1. Then, the program should compute
## X^2 + 3X + 4, leaving the register r13, and write it out.

### 0 read r1 --> r1 = X
### 1 mul r13 r1 r1 --> r13 = X^2
### 2 setn r2 3 --> r2 = 3
### 3 mul r3 r1 r2 --> r3 = X * 3 = 3X
### 4 addn r13 4 --> r1 = X^2 + 4
### 5 add r13 r13 r3 --> r13 = X^2 + 4 + 3X
### 6 write r13
### 7 halt