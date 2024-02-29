# CutePy Compiler README

## Overview
This repository contains the complete implementation of a compiler for a custom programming language named CutePy. CutePy is designed to offer a simplified programming experience while incorporating essential elements of Python. The compiler fully translates CutePy code into machine language, producing several output files that demonstrate the compiled code's functionality.

## Output Files
Upon running CutePy code, the compiler generates the following files:
- `OutputFile`: The main output from the compilation process.
- `file_with_quads.int`: Intermediate representation of the code in quadruples.
- `finalFile.asm`: The assembly code generated for RISC-V processors.

## Input Files
We provide five sample CutePy programs to illustrate the compiler's capabilities:
- `countdigits.cpy`: Counts the digits of a number.
- `factorial.cpy`: Computes the factorial of a number.
- `fibonacci.cpy`: Generates the Fibonacci sequence.
- `primes.cpy`: Identifies prime numbers.
- `paradeigmata_mazi.cpy`: A comprehensive file that includes all the above programs.

## Running the Compiler
To compile a CutePy program, use the following command in a Linux environment:
```
python3 cutePy_4001_4821.py <input_file>.cpy
```
Replace `<input_file>.cpy` with the name of the CutePy file you wish to compile.
