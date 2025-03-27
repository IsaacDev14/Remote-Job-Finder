const jobListings = document.getElementById("job-listings");
const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");
const locationFilter = document.getElementById("locationFilter");
const filterBtn = document.getElementById("filterBtn");
const categoryButtons = document.querySelectorAll(".category-btn");

const prevPageBtn = document.getElementById("prevPage");
const nextPageBtn = document.getElementById("nextPage");
const pageNumber = document.getElementById("pageNumber");


let jobs = [];
let filteredJobs = [];
let currentPage = 1;
const jobsPerPage = 8;

// Fetch jobs from JSON file located in github
async function fetchJobs() {
    try {
        const response = await fetch("https://raw.githubusercontent.com/IsaacDev14/Remote-Job-Finder/main/jobs.json"); // uses a link from github
        jobs = await response.json();
        filteredJobs = jobs; // Show all jobs initially
        displayJobs();
    } catch (error) {
        console.error("Error fetching jobs:", error);
    }
}

// Display jobs with pagination
function displayJobs() {
    jobListings.innerHTML = "";

    const start = (currentPage - 1) * jobsPerPage;
    const end = start + jobsPerPage;
    const jobsToShow = filteredJobs.slice(start, end);

    jobsToShow.forEach(job => {
        const jobCard = document.createElement("div");
        jobCard.classList.add("col-lg-3", "col-md-4", "col-sm-6", "mb-2"); // Responsive layout

        jobCard.innerHTML = `
            <div class="card shadow-sm">
                <img src="${job.image}" class="card-img-top" alt="${job.title}">
                <div class="card-body p-3">
                    <h5 class="card-title text-primary">${job.title}</h5>
                    <p class="card-text"><strong>${job.company}</strong> - ${job.location}</p>
                    <p class="card-text">${job.description.length > 100 ? job.description.substring(0, 100) + '...' : job.description}</p>
                    ${job.description.length > 100 ? `<a href="#" class="read-more" data-desc="${job.description}">Read more</a>` : ""}
                    <p class="card-text text-muted">${job.salary}</p>
                    <button class="btn btn-sm btn-primary apply-btn mt-2">Apply Now</button>
                </div>
            </div>
        `;

        // Add event listener for "Read more"
        jobCard.querySelector(".read-more")?.addEventListener("click", function (event) {
            event.preventDefault();
            this.previousElementSibling.textContent = this.dataset.desc; // Show full description
            this.remove(); // Remove "Read more" link after expanding
        });

        // Handle "Apply Now" button click
        const applyButton = jobCard.querySelector(".apply-btn");
        applyButton.addEventListener("click", function () {
            this.textContent = "You have successfully applied";
            this.classList.remove("btn-primary");
            this.classList.add("btn-success"); // Change button color to green
            this.disabled = true; // Disable button after clicking
        });

        jobListings.appendChild(jobCard);
    });

    updatePagination();
}

// Update pagination controls
function updatePagination() {
    pageNumber.textContent = currentPage;
    prevPageBtn.disabled = currentPage === 1;
    nextPageBtn.disabled = (currentPage * jobsPerPage) >= filteredJobs.length;
}

// Filter jobs based on search, category, and location
function filterData() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedCategory = categoryFilter.value;
    const selectedLocation = locationFilter.value;

    filteredJobs = jobs.filter(job =>
        (searchTerm === "" || job.title.toLowerCase().includes(searchTerm) || job.company.toLowerCase().includes(searchTerm)) &&
        (selectedCategory === "" || job.category === selectedCategory) &&
        (selectedLocation === "" || job.location === selectedLocation)
    );

    currentPage = 1; // Reset to first page
    displayJobs();
}

// Event Listeners
filterBtn.addEventListener("click", filterData);
searchInput.addEventListener("input", filterData);

// Reset job listing if search is cleared
searchInput.addEventListener("input", () => {
    if (searchInput.value === "") {
        filteredJobs = jobs;
        displayJobs();
    }
});

// Filter via category buttons
categoryButtons.forEach(button => {
    button.addEventListener("click", function () {
        categoryFilter.value = this.dataset.category;
        categoryFilter.dispatchEvent(new Event("change")); // Ensure UI updates
        filterData();
    });
});

// Pagination Controls
prevPageBtn.addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        displayJobs();
    }
});

nextPageBtn.addEventListener("click", () => {
    if (currentPage * jobsPerPage < filteredJobs.length) {
        currentPage++;
        displayJobs();
    }
});

// Load jobs on page load
document.addEventListener("DOMContentLoaded", fetchJobs);
