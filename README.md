# Assignment2
## Live application Links


[![Google Colab](https://img.shields.io/badge/colab-FFDF00?style=for-the-badge&logo=colab&logoColor=white)](https://colab.research.google.com/drive/1mOOuDCEp9ESbSsifeFDqJp3WskTJ8j32#scrollTo=xu2UBhqc0oET)
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1AgnwpCz5vmdYBHjGpfDjJot6-G8YAur_iSxXw-1CA3M/#0)


## Problem Statement

This project aims to streamline access to finance professional development resources by developing a data engineering solution that structures and aggregates content from the CFA Institute’s website.
The outcome will support an intelligent application to enhance finance professionals' learning experiences, demonstrated through comprehensive documentation and a GitHub repository showcasing the workflow and results.

## Project Goals

Key tasks include:
1. **Automated Web Scraping**: Extract and structure information from 224 refresher readings into a CSV dataset.
2. **PDF Text Extraction**: Utilize PyPDF2 and Grobid to extract text from PDF files, organizing it into structured text files.
3. **Database Integration**: Upload the structured data to a Snowflake database.
4. **Cloud Storage**: Store the dataset and text files in an AWS S3 bucket.

## Technologies Used
[![Scrapy](https://img.shields.io/badge/scrapy-109989?style=for-the-badge&logo=scrapy&logoColor=white)](https://docs.scrapy.org/en/latest/)
[![Playwright](https://img.shields.io/badge/playwright-FFFFFF?style=for-the-badge&logo=playwright&logoColor=green)](https://playwright.dev/docs/intro)
[![GROBID](https://img.shields.io/badge/GROBID-FFFFFF?style=for-the-badge&logo=GROBID&logoColor=black)](https://grobid.readthedocs.io/en/latest/Introduction/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/snowflake-0000FF?style=for-the-badge&logo=snowflake&logoColor=white)](https://docs.snowflake.com/ )
[![AWS](https://img.shields.io/badge/AWS-FFFFFF?style=for-the-badge&logo=Amazon&logoColor=yellow)](https://docs.aws.amazon.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FFFFFF?style=for-the-badge&logo=SQLAlchemy&logoColor=red)](https://docs.sqlalchemy.org/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-FFFFFF?style=for-the-badge&logo=PyPDF2&logoColor=grey)](https://pypdf2.readthedocs.io/)

## Data Sources

The webpages are being scraped from this main webpage:

https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=200&sort=%40refreadingcurriculumyear%20descending

The PDF Archives can be found Assignment2/Datasets/Sample_PDFs/


## Pre requisites
1. Python 3.6 or later from https://www.python.org/downloads
2. AWS credentials
3. Snowflake credentials
4. Docker

## Project Structure
```
├─ .gitignore
├─ Diagrams
│  ├─ Architecture Diagram.py
├─ Datasets
│  ├─ CFA.csv
│  ├─ Grobid
│  │  ├─ Grobid_RR_2024_l1_combined.txt
│  │  ├─ Grobid_RR_2024_l1_combined.xml
│  │  ├─ Grobid_RR_2024_l2_combined.txt
│  │  ├─ Grobid_RR_2024_l2_combined.xml
│  │  ├─ Grobid_RR_2024_l3_combined.txt
│  │  ├─ Grobid_RR_2024_l3_combined.xml
│  │  └─ metadata.csv
│  ├─ PyPDF
│  │  ├─ PyPDF_RR_2024_l1_combined.txt
│  │  ├─ PyPDF_RR_2024_l2_combined.txt
│  │  └─ PyPDF_RR_2024_l3_combined.txt
│  └─ Sample_PDFs
│     ├─ 2024-l1-topics-combined-2.pdf
│     ├─ 2024-l2-topics-combined-2.pdf
│     └─ 2024-l3-topics-combined-2.pdf
├─ Pwspider
│  ├─ Pwspider
│  │  ├─ WebScrapingandDatasetCreation.ipynb
│  │  ├─ __init__.py
│  │  ├─ items.py
│  │  ├─ middlewares.py
│  │  ├─ pipelines.py
│  │  ├─ settings.py
│  │  └─ spiders
│  │     ├─ CFA.csv
│  │     ├─ DEBUG.log
│  │     ├─ __init__.py
│  │     ├─ pwspidey.py
│  │     └─ requirements.txt
│  └─ scrapy.cfg
├─ README.md
└─ notebooks
   ├─ Cloud_storage_integration.ipynb
   ├─ PDF Extraction.ipynb
   ├─ SQLAlchemy_Snowflake_Database.py
   └─ WebScrapingandDatasetCreation.ipynb


```


## How to run Application locally

To run Web Scraping locally follow these steps:

1. Create a virtual environment on local setup and activate it.

   CLI MacOS: 
	python3 -m venv .venv
	source .venv/bin/activate

   CLI Windows:
	py -m venv .venv
	.venv\Scripts\activate

2. Install the requirements: scrapy, playwright. Install the requirements.txt from the path Assignment2/Pwspider/Pwspider/spider/
CLI on Terminal: pip install -r requirements.txt

3. To run the spider on terminal:
   - Naviage to folder Assignment2/Pwspider/Pwspider/spider/
   - Run the cli: "scrapy crawl pwspidey -o CFA.csv -s LOG_FILE=DEBUG.log" where pwspidey is the name of the spider, CFA.csv is where the scraped data is stored and DEBUG.LOG is the debug log for the process.

   To run the spider on Notebook environment:
   - Launch Jupyter notebook.
   - Navigate to Assignment2/Pwspider/Pwspider/ and open WebScrapingandDatasetCreation.ipynb
   - Change the evironment of the kernel to scraping environment.
   - Run the notebook.
  
Running Grobid Locally with Docker:

1. Install Docker: https://docs.docker.com/desktop/install/windows-install/

2. Choose a Grobid Docker Image: Lightweight Image 

```
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:latest
```

3. Start the Grobid Docker Container

PyPDF2: Requirements
```
   pip install PyPDF2
```
Snowflake Upload:
Requirements
1. SQLAlchemy installation
2. Pandas

Run the Jupyter notebook SQLAlchemy_Snowflake_Database.py in the path Assignment2/notebooks/ to upload the dataset to Snowflake DB

AWS S3 upload:
Requirements
1. S3 credentials

Run the Jupyter notebook Cloud_storage_integration.ipynb in the path Assignment2/notebooks/ to upload the dataset to AWS S3

## References
https://www.zenrows.com/blog/scrapy-playwright#why-use-playwright-with-scrapy\
https://github.com/kermitt2/grobid \
https://pypdf.readthedocs.io/en/stable/\
https://diagrams.mingrammer.com/\
https://github.com/ashrithagoramane/DAMG7245-Spring24/tree/main/repository_structure
     
## Learning Outcomes
1. Web scraping tools and techniques
2. PDF Extraction Tools and Techniques
3. SQL and AWS S3 upload methods 

## Team Information and Contribution 

Name | Contribution %| Contributions |
--- |--- | --- |
Nidhi Nitin Kulkarani 	| 35% |Web Scraping and Dataset Creation, Documentation, README |
Riya Singh 		| 35% |PDF Extraction, Grobid Local installation and PDF Extraction via Grobid and PyPDF2, Documentation, README |
Deepakraja Rajendran 	| 30% |Snowflake and Amazon S3 Database Upload, Cloud Storage Integration Diagram |
