# Kaggle Dev Ops

Everyone deserves automation including kagglers.

These are very early iterations of a repo to help automated some Kaggle tasks, especially for the Severstal competition.

## severstal-steel-defect-detection

### Features

**Submit CSV file to the public LB.** This will not upload any models or perform any predictions on the private test est. It does allow rapid iteration to go from a model that has predicted a CSV locally to a public LB score.

### Instructions

Tested on: Ubuntu 18.04

Setup the [kaggle api](https://github.com/Kaggle/kaggle-api)

You may need install cmake: `sudo apt install cmake`

Clone the repo: `git clone https://github.com/alekseynp/kaggle-dev-ops.git`

Enter the repo: `cd kaggle-dev-ops`

Go to severstal: `cd severstal-steel-defect-detection`

Initialize: `make init-csv-submission`

Submit: `SUBMISSION=/path/to/csv/file.csv make release-csv`

Click the link to the kernel and press the submit to competition button.

