# Assignment2
## Live application Links


[![Google Colab](https://img.shields.io/badge/colab-FFDF00?style=for-the-badge&logo=colab&logoColor=white)](https://colab.research.google.com/drive/1mOOuDCEp9ESbSsifeFDqJp3WskTJ8j32#scrollTo=xu2UBhqc0oET)
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1AgnwpCz5vmdYBHjGpfDjJot6-G8YAur_iSxXw-1CA3M/#0)
[![YouTube](https://img.shields.io/badge/youtube-ff0000?style=for-the-badge&logo=youtube&logoColor=white)]()

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
[![AWS](https://docs.aws.amazon.com/)]

## Data Sources

The webpages are being scraped from this main webpage:
https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=200&sort=%40refreadingcurriculumyear%20descending


## Pre requisites
*Define any prerequisites of softwares/knowledge base for the project*

## Project Structure
```
.
├── README.md
├── sqlalchemy
│   ├── 1_mysql.py
│   ├── 2_mysql.py
│   ├── 3_mysql.py
│   ├── 4_snowflake_sqlalchemy.py
│   ├── 5_snowflake.py
│   ├── 6_snowflake.py
│   ├── 7_snowflake.py
│   └── requirements.txt
├── streamlit
│   ├── Dockerfile
│   ├── README.md
│   ├── main.py
│   └── requirements.txt
└── streamlit-multipage
    ├── README.md
    ├── example.env
    ├── main.py
    ├── pages
    │   ├── 1_uber_nyc.py
    │   ├── 2_Plotting_Demo.py
    │   ├── 3_nexrad_station.py
    │   └── 4_test.py
    ├── requirements.txt
    └── streamlit_colab.ipynb
```

*You can generate the project tree using following tools*
*[Project Tree Generator](https://woochanleee.github.io/project-tree-generator)*
*[Generate from terminal](https://www.geeksforgeeks.org/tree-command-unixlinux/)*

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

## References
*All the external references must be listed down.*
     
## Learning Outcomes
*List the learning outcomes from the assignment/project*

## Team Information and Contribution 

Name | Contribution %| Contributions |
--- |--- | --- |
Nidhi Nitin Kulkarani 	| 33.33% |Web Scraping and Dataset Creation, Documentation, README |
Riya Singh 		| 33.33% |PDF Extraction, Documentation |
Deepakraja Rajendran 	| 33.33% |Database Upload, Cloud Storage Integration Diagram |
