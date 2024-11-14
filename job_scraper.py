import requests
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your actual App ID and Key from Adzuna
app_id = "193c05ba"
app_key = "16d40e8ae1f65fdfbbf8911ec9fb5d69"

# Adzuna API endpoint (correct URL format)
api_url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={app_key}&results_per_page=50"

# Make the API request
response = requests.get(api_url)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON data

    # Process and extract job listings
    job_listings = []
    for job in data['results']:
        job_title = job['title']
        company = job['company']['display_name']
        location = job['location']['display_name']
        salary_min = job.get('salary_min', 'N/A')
        salary_max = job.get('salary_max', 'N/A')
        job_url = job['redirect_url']
        
        # Append job details to the list
        job_listings.append([job_title, company, location, salary_min, salary_max, job_url])

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(job_listings, columns=["Job Title", "Company", "Location", "Salary Min", "Salary Max", "URL"])

    # Save data to CSV
    csv_file_path = "adzuna_job_listings.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"Job listings data saved to '{csv_file_path}'")

    # Load the CSV data back into a DataFrame for analysis and visualization
    df = pd.read_csv(csv_file_path)

    # Convert Salary Min and Max to numeric, handling 'N/A' values
    df['Salary Min'] = pd.to_numeric(df['Salary Min'], errors='coerce')
    df['Salary Max'] = pd.to_numeric(df['Salary Max'], errors='coerce')

    # Visualization: Most Common Job Titles
    plt.figure(figsize=(10, 6))
    df['Job Title'].value_counts().head(10).plot(kind='barh', color='skyblue')
    plt.title('Top 10 Most In-Demand Job Titles')
    plt.xlabel('Number of Listings')
    plt.ylabel('Job Title')
    plt.gca().invert_yaxis()  # Invert to have the most frequent on top
    plt.show()

    # Visualization: Average Salary by Location
    avg_salary_by_location = df.groupby('Location')[['Salary Min', 'Salary Max']].mean().dropna().sort_values(by="Salary Min", ascending=False).head(10)
    avg_salary_by_location.plot(kind='bar', figsize=(12, 6), color=['#FFA07A', '#20B2AA'])
    plt.title('Top 10 Locations by Average Minimum and Maximum Salary')
    plt.xlabel('Location')
    plt.ylabel('Average Salary')
    plt.show()

    # Visualization: Job Listings Concentration by Location
    plt.figure(figsize=(10, 6))
    df['Location'].value_counts().head(10).plot(kind='barh', color='lightgreen')
    plt.title('Top 10 Locations with the Most Job Listings')
    plt.xlabel('Number of Listings')
    plt.ylabel('Location')
    plt.gca().invert_yaxis()
    plt.show()

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
