from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine

from models import JobsInsert, JobsSelect, JobsUpdate
from service import Job

app = FastAPI()

engine = create_engine("sqlite:///my_database.db")

job = Job(engine)

SQLModel.metadata.create_all(engine)


@app.get("/jobs", response_model=list[JobsSelect])
def get_jobs(start: int | None = None, end: int | None = None):
    if start is not None and end is not None:
        return job.select_jobs(start, end)
    elif start is not None:
        return job.select_jobs(start=start)
    elif end is not None:
        return job.select_jobs(end=end)
    return job.select_jobs()


@app.get("/jobs/{job_id}", response_model=JobsSelect)
def get_job(job_id: int):
    result = job.select_job(job_id)
    if result is None:
        raise HTTPException(404, "Job not Found")
    return result


@app.post("/jobs")
def post_job(data: JobsInsert):
    job_id = job.create_job(data)
    if job_id is None:
        raise HTTPException(400, "Job not created")
    return job_id


@app.put("/jobs/{job_id}", response_model=JobsSelect)
def put_job(job_id: int, data: JobsUpdate):
    updated_job = job.update_job(job_id, data)
    if updated_job is None:
        raise HTTPException(400, "Job not updated")
    return updated_job


@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    deleted_job = job.remove_job(job_id)
    if deleted_job is None:
        raise HTTPException(400, "Job not deleted")
    return deleted_job
