
# Simple 2-Bit CPU Emulator

This is a simple Python implementation of a 2-bit CPU emulator. The CPU supports basic operations such as loading values from memory, storing values to memory, adding values from memory to a register, and removing values from memory.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/netflexs/CPU_Emulation.git
cd 2-bit-cpu-emulator
```

2. Run the `CPU_Emulation.py` script:

```bash
python CPU_Emulation.py
```

3. Define your program in the `cpu.py` file:

```python
# Example program
program = [
    0b0101,  # Load value from memory cell 1
    0b1010,  # Store value to memory cell 2
    0b1111,  # Add value from memory cell 1 to register
    0b1001   # Remove value from memory cell 1
]

cpu = CPU(memory_size=4)
cpu.run_program(program)
```

4. Customize the program as needed by modifying the `program` list in `cpu.py`.

## Instructions

- **Load**: `0b01`, followed by a 2-bit operand. Loads the value from the specified memory cell into the register.
- **Store**: `0b10`, followed by a 2-bit operand. Stores the value from the register into the specified memory cell.
- **Add**: `0b11`, followed by a 2-bit operand. Adds the value from the specified memory cell to the value in the register.
- **Remove**: `0b100`, followed by a 2-bit operand. Removes the value from the specified memory cell.

## Error Handling

- Invalid memory addresses: If the program tries to access a memory cell outside the valid range, an error will be raised.
- Program size exceeds memory capacity: If the program size exceeds the memory capacity of the CPU, an error will be raised.

Feel free to modify the `CPU` class in `CPU_Emulation.py` to add more features or improve error handling as needed.