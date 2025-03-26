import json
import random

# Expanded Categories
categories = [
    "Software Development", "Data Science", "Marketing", "Finance", "Human Resources",
    "Design", "Customer Support", "Education", "Cybersecurity", "Healthcare", "Legal",
    "Business Development", "Sales", "Engineering", "Operations", "Consulting", "Product Management",
    "Content Writing", "Journalism", "Public Relations", "Manufacturing", "Construction", "Aerospace",
    "Defense", "Hospitality", "Tourism", "Gaming", "Blockchain", "AI Research", "E-commerce", "Retail",
    "Supply Chain", "Agriculture", "Automotive", "Telecommunications", "Biotechnology", "Pharmaceuticals",
    "Energy", "Environmental Science", "Government", "Non-Profit"
]

# Expanded Company List
companies = [
    "Google", "Microsoft", "Amazon", "Facebook", "Tesla", "Netflix", "Spotify",
    "IBM", "Oracle", "Salesforce", "Stripe", "Shopify", "Airbnb", "Adobe", "LinkedIn", "Safaricom",
    "Apple", "Twitter", "Zoom", "Samsung", "Intel", "NVIDIA", "Cisco", "Siemens", "Dell", "HP", "Sony",
    "Twitch", "Snapchat", "Pinterest", "SpaceX", "Reddit", "Uber", "Lyft", "TikTok", "Huawei", "Alibaba",
    "WeWork", "Accenture", "Capgemini", "Deloitte", "Goldman Sachs", "JP Morgan", "Boeing", "Ford", "General Motors"
]

# Expanded Job Titles
job_titles = [
    "Software Engineer", "Data Analyst", "Machine Learning Engineer", "Marketing Manager",
    "Finance Specialist", "HR Recruiter", "UX/UI Designer", "Customer Support Agent",
    "Cybersecurity Analyst", "Legal Advisor", "Full Stack Developer", "Cloud Engineer",
    "Frontend Developer", "Backend Developer", "Project Manager", "DevOps Engineer",
    "Product Manager", "AI Research Scientist", "Game Developer", "Business Analyst",
    "SEO Specialist", "Social Media Manager", "Copywriter", "Technical Writer", "Solutions Architect",
    "Systems Administrator", "Network Engineer", "Biomedical Engineer", "Pharmacist", "Investment Banker",
    "Financial Analyst", "Blockchain Developer", "AI Ethics Consultant", "Data Engineer",
    "Robotics Engineer", "Environmental Consultant", "UX Researcher", "Growth Hacker",
    "Operations Manager", "Security Engineer", "Electrical Engineer", "Aerospace Engineer",
    "Telecommunications Specialist", "Agricultural Scientist", "Legal Compliance Officer",
    "Supply Chain Manager", "E-commerce Manager", "Video Game Tester", "AI Chatbot Developer"
]

# Expanded Locations
locations = [
    "Remote", "Hybrid", "USA", "Europe", "Canada", "UK", "India", "Germany", "Australia", "Kenya",
    "South Africa", "Japan", "China", "Singapore", "Brazil", "Mexico", "France", "Italy", "Netherlands",
    "Sweden", "Denmark", "Norway", "Finland", "Spain", "Ireland", "Argentina", "United Arab Emirates",
    "Saudi Arabia", "New Zealand", "South Korea", "Vietnam", "Malaysia"
]

# Generate job listings
num_jobs = 100  # Set the number of jobs
jobs = []

# List of available images (Assuming you have job1.jpg to job20.jpg)
image_filenames = [f"job{i}.jpg" for i in range(1, 21)]  

for i in range(1, num_jobs + 1):
    job_title = random.choice(job_titles)
    company = random.choice(companies)
    category = random.choice(categories)
    location = random.choice(locations)
    salary = f"Ksh {random.randint(150, 600)}k"

    job = {
        "id": i,
        "title": job_title,
        "company": company,
        "category": category,
        "location": location,
        "salary": salary,
        "description": f"Exciting opportunity for a {job_title} at {company}. Join our {category} team and make an impact.",
        "apply_link": f"https://example.com/job/{i}",
        "image": f"data/{random.choice(image_filenames)}"
    }
    jobs.append(job)

# Save jobs to a JSON file
with open("jobs.json", "w") as f:
    json.dump(jobs, f, indent=4)

print(f"✅ {num_jobs} jobs successfully generated in 'jobs.json' with more diversity!")
