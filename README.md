# Nand2Tetris – Building a Computer from First Principles

## Overview

This repository contains my implementations of selected projects from **Nand2Tetris – The Elements of Computing Systems** by Noam Nisan and Shimon Schocken.

The goal of Nand2Tetris is to understand how a computer works from the ground up, starting with basic logic gates and gradually building more complex hardware components.

This repository includes:

- Project 1 – Boolean Logic
- Project 2 – Boolean Arithmetic
- Project 3 – Sequential Logic
- Project 5 – Computer Architecture
- Nand2Tetris Capstone Project

Most hardware components are implemented using **Hardware Description Language (HDL)** and tested using the Nand2Tetris Hardware Simulator. The Capstone additionally involves Python, Hack Assembly, and the CPU Emulator.

---

## Projects

### Project 1 – Boolean Logic

**Objective:** Build fundamental logic gates using the NAND gate as the basic building block.

Implemented various combinational logic chips, including:

- Not
- And
- Or
- Xor
- Mux
- DMux
- Not16
- And16
- Or16
- Mux16
- Or8Way
- Mux4Way1
- Mux4Way16
- Mux8Way1
- Mux8Way16
- DMux4Way
- DMux8Way

**Key Concepts:**
- Boolean algebra
- Logic gates
- Combinational circuits
- Multiplexers and demultiplexers
- Bitwise operations

### Project 2 – Boolean Arithmetic

**Objective:** Build arithmetic circuits and implement the Arithmetic Logic Unit (ALU) of the Hack computer.

Implemented the following chips:

- HalfAdder
- FullAdder
- Add16
- Inc16
- ALU

**Key Concepts:**
- Binary addition
- Half adders and full adders
- 16-bit arithmetic
- Incrementers
- Arithmetic Logic Unit (ALU)
- Control bits and ALU operations

The ALU performs arithmetic and logical operations based on its control inputs.

### Project 3 – Sequential Logic

**Objective:** Build memory components that can store and retrieve information over time.

This project focuses on sequential circuits and the use of clocked logic to retain data.

**Key Concepts:**
- Sequential circuits
- Flip-flops
- Data storage
- Registers
- Program counter
- RAM architecture
- Memory addressing

These components form the memory foundation required by the Hack computer.

### Project 5 – Computer Architecture

**Objective:** Combine previously developed hardware components to construct the Hack computer.

Implemented the main components:

- CPU
- Memory
- Computer

**Key Concepts:**
- CPU architecture
- Instruction decoding
- ALU integration
- Registers and memory
- Instruction execution
- Fetch-decode-execute cycle
- Computer architecture

The CPU executes Hack machine-language instructions, while the Memory and Computer chips integrate the hardware components into a complete computer system.

---

## Capstone Project

The Capstone Project brings together the concepts learned throughout Nand2Tetris.

It consists of three parts.

### Part A – Hardware Implementation

Implementation and integration of the Hack computer's hardware components using HDL.

Components include:

- CPU.hdl
- Memory.hdl
- Computer.hdl

### Part B – Hack Assembly Language Assembler

Developed a custom Hack assembler using Python.

**Features:**
- Converts Hack assembly (`.asm`) programs into 16-bit binary machine code (`.hack`).
- Implements a two-pass assembly process.
- Handles A-instructions and C-instructions.
- Resolves labels and symbols.
- Supports predefined symbols and variable allocation.
- Detects duplicate label definitions and displays warnings.

**Testing:**

The assembler was tested using the following programs:

- Add
- Max
- Rect
- Pong

The generated machine-code outputs were compared with the official reference outputs using a custom comparison script.

All four comparisons produced identical results.

The additional duplicate-label warning feature was also tested.

### Part C – Keyboard-Controlled Box

Developed a Hack Assembly program (`Box.asm`) that displays a black rectangular box on the Hack screen while a key is pressed.

**Program Behaviour:**
- Pressing a key displays the box.
- Releasing the key clears the box.
- The program continuously checks keyboard input.

**Personal Configuration:**

| Parameter | Value |
|---|---:|
| Personal Number (K) | 29 |
| K mod 4 | 1 |
| K mod 3 | 2 |
| Starting Row | 29 |
| Box Height | 20 rows |
| Box Width | 32 pixels |
| Starting Position | Left edge of screen |

The box width is calculated using:

`16 × ((K mod 4) + 1)`

For K = 29:

`16 × ((29 mod 4) + 1) = 32 pixels`

The program was assembled using the custom Python assembler developed in Part B and executed in the Nand2Tetris CPU Emulator.

---

## Repository Structure

```text
Nand2Tetris/
│
├── Project1/
│   └── HDL implementations and test files
│
├── Project
