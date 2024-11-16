Job Listings Web Scraper and Data Analyzer

Overview

This project is a Python-based web scraper and data analysis tool that collects job listings from the Adzuna API. It extracts relevant information such as job titles, locations, salaries, and links to the original job postings. The data is saved in a CSV file for further use and visualized through charts and graphs to analyze trends in job availability, salaries, and job concentrations by location.

Features

Fetches job listings from the Adzuna API.

Saves the retrieved data in a CSV file for offline analysis.

Analyzes the data to identify trends in job demand and salary distributions.

Visualizes data using matplotlib to create clear and insightful graphs.

Installation

Clone the repository:

git clone <https://github.com/priyankatyagi455/Adzuna-Job-Market-Insights.git>  

cd <Adzuna-Job-Market-Insights> 

Set up a virtual environment (optional but recommended):

python -m venv env  

source env/bin/activate  # For macOS/Linux

env\Scripts\activate     # For Windows  

Install the required dependencies:
pip install -r requirements.txt  
Obtain an Adzuna API key:
Sign up at Adzuna Developer Portal.
Create an application to get your App ID and API Key.
Update the script with your Adzuna API credentials:
Open the Python script and replace placeholders for APP_ID and APP_KEY with your Adzuna credentials.
Usage
Run the script to fetch job data:
python job_scraper.py  
View the output:
The data will be saved in a file named adzuna_job_listings.csv.
Graphs showing trends will appear in a separate window during execution.
Open the CSV file to explore the retrieved job data, which includes:
Job Titles
Locations
Salaries
Links to full job details
Visualizations
Job Demand by Title: A bar chart showing the most frequently occurring job titles.
Salary Distribution: A histogram of salaries to understand income trends.
Job Locations: A pie chart or bar chart to highlight areas with the most job listings.
File Structure
plaintext
project/  
├── job_scraper.py       # Main Python script for scraping and analysis  
├── adzuna_job_listings.csv # Output file containing scraped job data  
├── LICENSE              # License for the project  
├── README.md            # Project overview and instructions  
└── requirements.txt     # List of required Python packages  

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

Security Note

Please ensure that your Adzuna API credentials (App ID and API Key) are not exposed publicly when sharing the project. Consider using environment variables to manage sensitive information.

Acknowledgments

Data Source: Adzuna API
Libraries Used: Python, Requests, Matplotlib, Pandas
