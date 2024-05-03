class CPU:
    def __init__(self, memory_size=4):
        self.memory_size = memory_size
        self.memory = [0] * memory_size
        self.register = 0

    def fetch_instruction(self, address):
        if address < 0 or address >= self.memory_size:
            raise ValueError("Invalid memory address")
        return self.memory[address]

    def decode_instruction(self, instruction):
        opcode = instruction >> 2
        operand = instruction & 0b11
        return opcode, operand

    def execute_instruction(self, opcode, operand):
        if opcode == 0:
            pass  # No operation
        elif opcode == 1:
            if operand < 0 or operand >= self.memory_size:
                raise ValueError("Invalid memory address")
            self.register = self.memory[operand]
        elif opcode == 2:
            if operand < 0 or operand >= self.memory_size:
                raise ValueError("Invalid memory address")
            self.memory[operand] = self.register
        elif opcode == 3:
            if operand < 0 or operand >= self.memory_size:
                raise ValueError("Invalid memory address")
            self.register += self.memory[operand]
        elif opcode == 4:
            if operand < 0 or operand >= self.memory_size:
                raise ValueError("Invalid memory address")
            self.memory[operand] = 0

    def run_program(self, program):
        if len(program) > self.memory_size:
            raise ValueError("Program size exceeds memory capacity")
        
        for address, instruction in enumerate(program):
            if address >= self.memory_size:
                raise ValueError("Program size exceeds memory capacity")
            self.memory[address] = instruction

        for address in range(len(program)):
            instruction = self.fetch_instruction(address)
            opcode, operand = self.decode_instruction(instruction)
            try:
                self.execute_instruction(opcode, operand)
                print(f"Instruction: {bin(instruction)} -> Opcode: {opcode}, Operand: {operand}")
                print(f"Memory: {self.memory}, Register: {bin(self.register)}")
            except ValueError as e:
                print(f"Error: {e}")
                break

# Example program
program = [
    0b0101,  # Load value from memory cell 1
    0b1010,  # Store value to memory cell 2
    0b1111,  # Add value from memory cell 1 to register
    0b1001,# Remove value from memory cell 1
    0b0101,  # Load value from memory cell 1
    0b1010,  # Store value to memory cell 2
    0b1111,  # Add value from memory cell 1 to register
    0b1001

]

cpu = CPU(memory_size=8)
cpu.run_program(program)
