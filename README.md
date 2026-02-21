CSC 4210 Computer Architecture
Task 1 – Data Systems
Lucia Aguirre

HOW TO RUN

python data_systems.py 123 BIN
python data_systems.py -45 HEX

FORMAT

python data_systems.py <decimal_number> <DEC|BIN|HEX>

RUN TESTS

python -m unittest -v

DESCRIPTION

- Parses signed decimal input
- Converts to 32‑bit Two’s Complement
- Outputs DEC / BIN / HEX
- Detects overflow
- Uses saturation instead of wrap-around
