# FinalProject
#  ISA Description and OPcodes

## ISA

| Instruction | OPcode | Description                | Format                |
| ----------- | ------ | -------------------------- | --------------------- |
| `add`       | `00`   | Adds rA to rB              | `00 rA rB`            |
| `sub`       | `01`   | Subtracts rA from rB       | `01 rA rB`            |
| `mul`       | `02`   | Multiplies rB by rA        | `02 rA rB`            |
| `div`       | `03`   | Divides rB by rA           | `03 rA rB`            |
|             |        |                            |                       |
| `mrmov`     | `40`   | Moves D(rB) to rA          | `40 rA rB D` (1 byte) |
| `rmmov`     | `50`   | Moves rA to D(rB)          | `50 rA rB D` (1 byte) |
| `rrmov`     | `60`   | Moves rB to rA             | `60 rA rB`            |
| `irmov`     | `70`   | Moves V to rA              | `70 rA 0 V` (1 byte)  |
|             |        |                            |                       |
| `jmp`       | `90`   | Unconditional jump to Dest | `90 FF Dest` (1 byte) |
| `jle`       | `91`   | Jump <= to Dest            | `91 FF Dest` (1 byte) |
| `jl`        | `92`   | Jump < to Dest             | `92 FF Dest` (1 byte) |
| `je`        | `93`   | Jump == to Dest            | `93 FF Dest` (1 byte) |
| `jne`       | `94`   | Jump != to Dest            | `94 FF Dest` (1 byte) |
| `jg`        | `95`   | Jump > to Dest             | `95 FF Dest` (1 byte) |
| `jge`       | `96`   | Jump <= to Dest            | `96 FF Dest` (1 byte) |
|             |        |                            |                       |
| `halt`      | `A0`   | Stops execution            | `A0`                  |
| `push`      | `B1`   | Push rA to stack           | `B1 rA 0 01`          |
| `pop`       | `C0`   | Pop rA from stack          | `C0 rA 0 01`          |
| `call`      | `D0`   | Call destination	          | `D0 FF Dest` (1 byte) |
| `ret`       | `E0`   | Return %eax		            | `E0`                  | 


## Registers
| Register | Code |
| -------- | ---- |
| %eax     | 0    |
| %ebx     | 1    |
| %ecx     | 2    |
| %edx     | 3    |
| %rsp     | 4    |
| %rbp     | 5    |

## Flags
| Flag      | Code |
| --------- | ---- |
| No Flag   | 00   |
| Neg Flag  | 01   |
| Zero Flag | 10   |
