from typing import List, Optional

from sqlmodel import Field, SQLModel

# DB location
DATABASE_URL = "postgresql://postgres:0@localhost/a"


class Subject(SQLModel, table=True):
    __tablename__ = "Subjects"

    id: int = Field(primary_key=True)
    name: str
    name_cn: Optional[str] = None
    infobox: Optional[str] = None
    platform: int
    summary: str
    nsfw: bool
    score: float
    rank: int
    date: str
    favorite_wish: int
    favorite_done: int
    favorite_doing: int
    favorite_on_hold: int
    favorite_dropped: int
    series: bool

    tags: List[str] = Field(default=[])
    score_details_1: int
    score_details_2: int
    score_details_3: int
    score_details_4: int
    score_details_5: int
    score_details_6: int
    score_details_7: int
    score_details_8: int
    score_details_9: int
    score_details_10: int

    # Define method to store the tags as a list of strings (JSON-like field)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # You can implement any additional initialization logic here

    # You can add methods for advanced querying or manipulation if needed
