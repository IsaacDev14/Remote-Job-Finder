import json
import random

# Define sample data
categories = [
    "Software Development", "Data Science", "Marketing", "Finance", "Human Resources",
    "Design", "Customer Support", "Education", "Cybersecurity", "Healthcare", "Legal"
]

companies = [
    "Google", "Microsoft", "Amazon", "Facebook", "Tesla", "Netflix", "Spotify",
    "IBM", "Oracle", "Salesforce", "Stripe", "Shopify", "Airbnb", "Adobe", "LinkedIn", "Safaricom"
]

job_titles = [
    "Software Engineer", "Data Analyst", "Machine Learning Engineer", "Marketing Manager",
    "Finance Specialist", "HR Recruiter", "UX/UI Designer", "Customer Support Agent",
    "Cybersecurity Analyst", "Legal Advisor", "Full Stack Developer", "Cloud Engineer",
    "Frontend Developer", "Backend Developer", "Project Manager", "DevOps Engineer"
]

locations = ["Remote", "Hybrid", "USA", "Europe", "Canada", "UK", "India", "Germany", "Australia", "Kenya"]

# Generate job listings
num_jobs = 1000  # Set the number of jobs
jobs = []

# List of available images (Assuming you have job1.jpg to job10.jpg)
image_filenames = [f"job{i}.jpg" for i in range(1, 11)]  

for i in range(1, num_jobs + 1):
    job = {
        "id": i,
        "title": random.choice(job_titles),
        "company": random.choice(companies),
        "category": random.choice(categories),
        "location": random.choice(locations),
        "salary": f"ksh {random.randint(150, 250)}k",
        "description": f"Exciting opportunity as a {random.choice(job_titles)} at {random.choice(companies)}.",
        "apply_link": f"https://example.com/job/{i}",
        "image": f"data/{random.choice(image_filenames)}" # Assign random image
    }
    jobs.append(job)

# Save jobs to a JSON file
with open("jobs.json", "w") as f:
    json.dump(jobs, f, indent=4)

print(f"✅ {num_jobs} remote jobs successfully generated in 'jobs.json' with images!")
