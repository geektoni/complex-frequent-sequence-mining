# Sequential Pattern Mining with Complex Structure
Evaluation of an approximate approach on synthetic and medical data.

## Main Programs:

The code needs **Python 3.0** in order to be run.

- `main.py`
	-	It manages the three algorithms to assess the Sequential Pattern Mining problem.
	-	It contains an helper that provide all the information to run the code.
- `dataset_generator.py`
	- It contains a simple code to generate a random dataset of sequences of complex structure.
	- There is the gen.sh to generate automatically a set of datasets throught this script
	
## Supporting code
	- print_graphs.py -> Support program to generate graphics on results
	- comparator.py   -> Support program to compare .db outputs

## Project Structure
The directory is structured as follow:
-	`datasets`
	-	It contains the input datasets, generated or not by the dataset_generator
	-	if generated, the name contains the information about the setting used
-	`experiments` 
	-	It contains the csv output data of the main program
	-	Each row contains specific information about a single algorithm execution
-	`results` dir 
	-	It contains the .db output data of the main program
	-	Each file contains the frequent sequences the main program found
	-	The name define the algorithm used and information to recover the input data

## Synthetic Medical Dataset
https://synthetichealth.github.io/synthea/
