# Data Processing Toolkit 👨‍💻

This is a labling tool designated for environmental variable labling, where user would be prompt with statements, and they would classify the statement whether it falls under environmental variable. The result would be collected into the `annotation_01.csv` file and later used for language model training.

## Requirements

- **Python** version 3.6 or higher

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/henryaudi/ClassificationCollector.git
```

## Usage

Before running the program, ensure you have an input CSV file prepared. By default, the program uses `"annotation_01.csv"` as the input file. If you wish to use a different file, you can configure this by modifying `classifier_tool.py`. On line 57, change `input_csv = 'annotation_01.csv'` to `input_csv = 'name_of_your_file.csv'`, where `'name_of_your_file.csv'` is the name of your input file.

To start classifying statements in the CSV file and generate an annotated CSV file, follow these steps:

1. **Make sure your input CSV file is formatted correctly, with two major columns: "file name" and "Environmental Statement".**
2. **Navigate to the project repository**
```bash
cd ClassificationCollector
```
3. **Execute the classifier tool by running:**
```bash
   python classifier_tool.py
```
4. **Follow the instructions in the command window and provide with your answer, below is a sample input:**
```bash
ClassificationCollector>python classifier_tool.py
Please enter your user ID or type 'EXIT' to quit: henry
------------------------------------------------
File Name: f2210f--2017
Statement: For 2017, the personal exemption remains at $4,050.
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------------------------------------
File Name: f2210f--2017
Statement: itemized deductions for taxpayers with adjusted gross incomes above $156,900 may be reduced
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------------------------------------
File Name: f2210f--2017
Statement: If you are an individual, estate, or trust and at least two-thirds of your 2016 or 2017 gross income is from farming or fishing, use Form 2210-F to see if you owe a penalty for underpaying your estimated tax.
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------------------------------------
File Name: f2210f--2017
Statement: If you checked box A or B in Part I of Form 2210-F, you must figure the penalty yourself and attach the completed form to your return.
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------------------------------------
File Name: f2210f--2017
Statement: If you didn’t check box A or B in Part I, you don’t need to figure the penalty or file Form 2210-F.
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------------------------------------
File Name: f2210f--2017
Statement: If you owe the penalty, the IRS will send you a bill.
Is this an environmental statement? (0: No, 1: Yes, 2: Uncertain): 1
------------------The End------------------
---------------Thank you!------------------
```
6. **Have fun! 🦥**

## Author
**Shangjie Zheng**

- **Affiliation:** Southern Methodist University
- **E-mail:** [shangjiehz@gmail.com](mailto:shangjiehz@gmail.com)

Feel free to reach out for any question or contributions to the project.
