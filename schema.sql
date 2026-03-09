CREATE TABLE jobs(
    id SERIAL PRIMARY KEY,
    company VARCHAR(255),
    job_title VARCHAR(255),
    salary VARCHAR(255),
    description TEXT,
    extracted_skills TEXT,
    seniority_level VARCHAR(255),
    notes TEXT,
    date_posted DATE,
    date_applied DATE,
    status VARCHAR(50)
);