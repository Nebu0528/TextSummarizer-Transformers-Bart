#!/bin/bash

# Compile the C program
echo "Compiling write_summary.c..."
gcc write_summary.c -o write_summary


# Activate the Python virtual environment
if [ ! -d "env" ]; then
    echo "No Virtual Environment Found. Follow readme.md instructions."
    exit 1
fi

# Run script
python summarizer.py

deactivate
echo "Execution completed."
