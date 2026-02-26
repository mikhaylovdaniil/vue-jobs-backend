from sqlmodel import Session, select

from models import Jobs


class Job:
    def __init__(self, engine):
        self.session = Session(engine)

    def __del__(self):
        self.session.close()

    def select_jobs(self, start: int | None = None, end: int | None = None):
        stm = select(Jobs)
        if start is not None and end is not None:
            stm = stm.where(Jobs.id >= start).where(Jobs.id < end)
        elif start is not None:
            stm = stm.where(Jobs.id >= start)
        elif end is not None:
            stm = stm.where(Jobs.id < end)
        return self.session.exec(stm).all()

    def select_job(self, job_id: int):
        pass  # TODO: select job from db

    def create_job(self, job: dict):
        pass  # TODO: insert job into db

    def update_job(self, job_id: int, job: dict):
        pass  # TODO: update job in db

    def remove_job(self, job_id: int):
        pass  # TODO: delete job from db
