.ONESHELL:

.PHONY: init-csv-submission
init-csv-submission:
	set -ex

	rm -rf submission_csv
	mkdir -p submission_csv

	kaggle datasets init -p submission_csv
	mv submission_csv/dataset-metadata.json dataset-csv-metadata.json
	sed -i 's/INSERT_TITLE_HERE/severstal_csv_submission/g' dataset-csv-metadata.json
	sed -i 's/INSERT_SLUG_HERE/severstal_csv_submission/g' dataset-csv-metadata.json

	kaggle kernels init -p submission_csv
	mv submission_csv/kernel-metadata.json kernel-csv-metadata.json
	sed -i 's/INSERT_KERNEL_SLUG_HERE/severstal-csv-submission/g' kernel-csv-metadata.json
	sed -i 's/INSERT_TITLE_HERE/severstal-csv-submission/g' kernel-csv-metadata.json
	sed -i 's/INSERT_CODE_FILE_PATH_HERE/kernel.py/g' kernel-csv-metadata.json
	sed -i 's/Pick one of: {python,r,rmarkdown}/python/g' kernel-csv-metadata.json
	sed -i 's/Pick one of: {script,notebook}/script/g' kernel-csv-metadata.json

	USERNAME=$(kaggle config view | grep username:* | cut -c 13-)
	sed -i 's#"dataset_sources": \[\]#"dataset_sources": \["${USERNAME}/severstal_csv_submission"\]#' kernel-csv-metadata.json
	sed -i 's#"competition_sources": \[\]#"competition_sources": \["severstal-steel-defect-detection"]#' kernel-csv-metadata.json

	cp dataset-csv-metadata.json submission_csv/dataset-metadata.json
	cp kernel_csv.py submission_csv/kernel.py
	kaggle datasets create -p submission_csv

.PHONY: release-csv
release-csv:

	rm -rf submission_csv
	mkdir -p submission_csv

	cp kernel-csv-metadata.json submission_csv/kernel-metadata.json
	cp dataset-csv-metadata.json submission_csv/dataset-metadata.json
	cp kernel_csv.py submission_csv/kernel.py
	cp $(SUBMISSION) submission_csv/out.csv

	kaggle datasets version -m "$(SUBMISSION)" -p submission_csv -r tar
	kaggle kernels push -p submission_csv/
