from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Companies(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    contactEmail: str | None = None
    contactPhone: str | None = None

    jobs: list["Jobs"] | None = Relationship(back_populates="company")


class Jobs(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    type: str
    location: str
    description: str
    salary: str

    company_id: int | None = Field(default=None, foreign_key="companies.id")
    company: Companies | None = Relationship(back_populates="jobs")


class JobsSelect(SQLModel):
    id: int | None = Field(default=None)
    title: str
    type: str
    location: str
    description: str
    salary: str

    company: Companies | None = Field(default=None)


class JobsInsert(SQLModel):
    title: str
    type: str
    location: str
    description: str
    salary: str


class JobsUpdate(SQLModel):
    title: str | None = Field(default=None)
    type: str | None = Field(default=None)
    location: str | None = Field(default=None)
    description: str | None = Field(default=None)
    salary: str | None = Field(default=None)
