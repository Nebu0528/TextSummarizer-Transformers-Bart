# Text Summarizer

A text summarizer built using Hugging Face's `transformers` library in Python to summarize the text and a C program to write the summary in a .txt file The bash script checks if the virtual environments exists, compiles the C program and runs the Python Script.

## Features
- **Terminal Tnterface**: Users can input the text to be summarized on the command line
- **Summarizes text using Hugging Face's BART model**.
- **Outputs the summarized text to a `.txt` file using a C program.**
- **Includes a Bash Script** to handle compilation and running the program.

## Dependencies
- **Python 3.7+**
- **GCC** (for compiling the C program)
- **Bash** (for running the bash script)
- **Pip** for managing Python packages

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Nebu0528/TextSummarizer-Transformers-Bart.git
    cd text_summarizer
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    - **On macOS/Linux**:
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```

3. **Install the Python dependencies**:
    ```bash
    pip install transformers torch
    ```
    3.1 **Recommended Versions**:
    ```bash
    transformers==4.31.0
    torch==2.4.1
    ```

## Usage

### Option 1: Bash Script Usage

1. **Make the bash script executable** (only needed once):
    ```bash
    chmod +x run_summarizer.sh
    ```

2. **Run the bash script**:
    ```bash
    ./run_summarizer.sh
    ```

   - The script will do the following:
     - Compile the C program (`write_summary.c`) to create a text file to write into.
     - Activate a Python virtual environment (if available).
     - Run the Python script to summarize text.
     - Write a summarized text to a `summary_output.txt` file using the C program.

3. **Deactivation**: Once the script finishes its execution, it will deactivate the python environment

### Option 2: Manually Running the Programs

1. **Compile the C program**:
    ```bash
    gcc write_summary.c -o write_summary
    ```

2. **Activate the Python virtual environment (Optional)**:
    - **On Windows**:
      ```bash
      .\env\Scripts\activate
      ```
    - **On macOS/Linux**:
      ```bash
      source env/bin/activate
      ```

3. **Run the Python script**:
    ```bash
    python app.py
    ```

4. **Deactivate the virtual environment**:
    ```bash
    deactivate
    ```

## Example

Running the program (either using the bash script or manually), it will prompt you to enter the text to be summarized:

**Sample Input Text:**
- Manage access in AWS by creating policies and attaching them to IAM identities (users, groups of users, or roles) or AWS resources. A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. AWS evaluates these policies when an IAM principal (user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON documents. AWS supports six types of policies: identity-based policies, resource-based policies, permissions boundaries, Organizations service control policies (SCPs), access control lists (ACLs), and session policies.
- [Reference Link](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

**Summarized Output:**
- A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON documents. 

## Future Improvements
- Have a parameter that specifies how many words it should be summarized to 
- Option to output it to different file types (word, pdf etc..)?
