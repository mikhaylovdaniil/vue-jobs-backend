from fastapi import FastAPI, HTTPException

app = FastAPI()


# Not api functions


def select_jobs(start: int | None = None, end: int | None = None):
    pass  # TODO: select jobs from db


def select_job(job_id: int):
    pass  # TODO: select job from db


def create_job(job: dict):
    pass  # TODO: insert job into db


def update_job(job_id: int, job: dict):
    pass  # TODO: update job in db


def remove_job(job_id: int):
    pass  # TODO: delete job from db


# =======================


@app.get("/jobs")
def get_jobs(start: int | None = None, end: int | None = None):
    if start is not None and end is not None:
        return select_jobs(start, end)
    elif start is not None:
        return select_jobs(start=start)
    elif end is not None:
        return select_jobs(end=end)
    return select_jobs()


@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    job = select_job(job_id)
    if job is None:
        raise HTTPException(404, "Job not Found")
    return job


@app.post("/jobs")
def post_job(job: dict):
    job_id = create_job(job)
    if job_id is None:
        raise HTTPException(400, "Job not created")
    return job_id


@app.put("/jobs/{job_id}")
def put_job(job_id: int, job: dict):
    updated_job = update_job(job_id, job)
    if updated_job is None:
        raise HTTPException(400, "Job not updated")
    return updated_job


@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    deleted_job = remove_job(job_id)
    if deleted_job is None:
        raise HTTPException(400, "Job not deleted")
    return deleted_job
