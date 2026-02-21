"""
CSC 4210/6210 Computer Architecture — Spring 2026
Processor Design Semester Project — Task 1: Data Systems

Author: Lucia Aguirre
"""

import sys

MIN_INT32 = -(2**31)
MAX_INT32 = (2**31) - 1
MASK_32   = 0xFFFFFFFF


def parse_decimal_input(s: str) -> int:
    return int(s.strip(), 10)


def detect_overflow_and_saturate(x: int):
    overflow = 1 if (x < MIN_INT32 or x > MAX_INT32) else 0
    if x > MAX_INT32:
        return MAX_INT32, overflow, 1
    if x < MIN_INT32:
        return MIN_INT32, overflow, 1
    return x, overflow, 0


def dec_to_bin32_twos_complement(x: int) -> str:
    unsigned_32 = x & MASK_32
    return format(unsigned_32, "032b")


def bin32_to_hex8(bin32: str, prefix=True) -> str:
    value = int(bin32, 2)
    hx = format(value, "08X")
    return ("0x" + hx) if prefix else hx


def bin32_to_signed_decimal(bin32: str) -> int:
    unsigned = int(bin32, 2)
    if (unsigned & (1 << 31)) != 0:
        return unsigned - (1 << 32)
    return unsigned


def format_output(final_int32: int, fmt: str) -> str:
    fmt = fmt.strip().upper()
    bin32 = dec_to_bin32_twos_complement(final_int32)

    if fmt == "DEC":
        return str(final_int32)
    if fmt == "BIN":
        return bin32
    if fmt == "HEX":
        return bin32_to_hex8(bin32, prefix=True)

    raise ValueError("Format must be DEC, BIN, or HEX")


def convert_invocation(decimal_str: str, fmt: str):
    x = parse_decimal_input(decimal_str)
    x_clamped, overflow, saturated = detect_overflow_and_saturate(x)
    value_out = format_output(x_clamped, fmt)

    return {
        "value_out": value_out,
        "overflow": overflow,
        "saturated": saturated,
    }


def main(argv):
    if len(argv) != 3:
        print("Usage: python3 data_systems.py <decimal_int> <DEC|BIN|HEX>")
        return 2

    decimal_str = argv[1]
    fmt = argv[2]

    try:
        result = convert_invocation(decimal_str, fmt)
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

    print(f"value_out: {result['value_out']}")
    print(f"overflow: {result['overflow']}")
    print(f"saturated: {result['saturated']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
