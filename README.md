#Team-ngeuss

A python solution to the 2016 google hashcode practise problem, as discussed and implemented by Andela's team-ngeuss.
More details on the team-based programming competition can be found [here](https://hashcode.withgoogle.com/). The problem description can also be obtained from
[this](https://drive.google.com/file/d/0B1GGqiPBaS6AWjF6d0pHOVcxaFU/view?usp=sharing) link.

## Installation

Clone the Repo
```bash
  git clone https://github.com/andela-bkagia/team-ngeuss.git
```

## How to run

Google provides input files for the challanges. You may download them separately to run them against our solution.
However, a handy little script has been included for the creation of arbitrary input files. You just give it the number of files you want to generate and they are created in the `input` folder.
```bash
  python generate_input_files.py 3
```
This creates 3 input files in an `/input` directory named:
  * file_1.in
  * file_2.in
  * file_3.in
  
Once you have input files, run the main script (`main.py`) in the root directory, with the path to the input file as a command-line argument.
For instance, to run with the generated file_1.in
```bash
  python main.py input/file_1.in
```
This will run the program and generate an output file in the `output` directory, named `output_ile.out`

## Contributing

  Open issues.
