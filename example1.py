from turing_machine import TuringMachine

machine = TuringMachine(
    {
        ('q0', '#'): ('saw_#', '#', 'R'),
        ('saw_#', '#'): ('saw_##', '#', 'R'),
        ('saw_##', ''): ('qa', '', 'R'),
    }
)

while True:
    input = input("Input: ")
    print("Accepted?", machine.accepts(input))
