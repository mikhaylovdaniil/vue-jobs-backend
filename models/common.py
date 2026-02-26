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
