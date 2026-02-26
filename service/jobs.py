from sqlmodel import Session, select

from models import Jobs, JobsInsert, JobsSelect, JobsUpdate


class Job:
    def __init__(self, engine):
        self.session = Session(engine)

    def __del__(self):
        self.session.close()

    def select_jobs(self, start: int | None = None, end: int | None = None):
        stm = select(Jobs)
        if start is not None and end is not None:
            stm = stm.where(Jobs.id >= start).where(Jobs.id < end)  # type: ignore
        elif start is not None:
            stm = stm.where(Jobs.id >= start)  # type: ignore
        elif end is not None:
            stm = stm.where(Jobs.id < end)  # type: ignore
        result = self.session.exec(stm).all()
        return_value = []
        for row in result:
            return_value.append(
                JobsSelect(
                    id=row.id,
                    title=row.title,
                    type=row.type,
                    location=row.location,
                    description=row.description,
                    salary=row.salary,
                    company=row.company,
                )
            )
        return return_value

    def select_job(self, job_id: int):
        stm = select(Jobs).where(Jobs.id == job_id)
        result = self.session.exec(stm).first()
        if result is None:
            return None
        return JobsSelect(
            id=result.id,
            title=result.title,
            type=result.type,
            location=result.location,
            description=result.description,
            salary=result.salary,
            company=result.company,
        )

    def create_job(self, job: JobsInsert):
        jobRow = Jobs(
            title=job.title,
            type=job.type,
            location=job.location,
            description=job.description,
            salary=job.salary,
        )

        self.session.add(jobRow)
        self.session.commit()

        return jobRow.id

    def update_job(self, job_id: int, job: JobsUpdate):
        stm = select(Jobs).where(Jobs.id == job_id)
        updated_job = self.session.exec(stm).first()

        if updated_job is None:
            return None

        # Updating only not None attrs
        for name, value in job.__dict__.items():
            if value is not None:
                setattr(updated_job, name, value)

        self.session.add(updated_job)
        self.session.commit()

        return updated_job

    def remove_job(self, job_id: int):
        pass  # TODO: delete job from db
