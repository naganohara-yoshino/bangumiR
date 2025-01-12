import uuid
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


# -------------------- 条目（Subject）模型 --------------------
class Subject(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    type: int  # 1: 漫画, 2: 动画, 3: 音乐, 4: 游戏, 6: 三次元
    name: str = Field(max_length=255)
    name_cn: str | None = Field(default=None, max_length=255)
    infobox: str | None = Field(default=None, max_length=1024)
    platform: str | None = Field(default=None, max_length=255)
    summary: str | None = Field(default=None, max_length=1024)
    nsfw: bool = False  # 是否为NSFW
    date: datetime | None = Field(default=None)
    favorite: str | None = Field(default=None, max_length=50)  # 想看、看过、在看等状态
    series: bool = False  # 是否为系列作品
    tags: str | None = Field(default=None, max_length=255)  # 标签
    score: float | None = Field(default=None)  # 评分
    score_details: str | None = Field(default=None, max_length=1024)  # 评分细节
    rank: int | None = Field(default=None)  # 类别内排名

    # 作品与人物的关系
    characters: list["SubjectCharacter"] = Relationship(back_populates="subject")
    persons: list["SubjectPerson"] = Relationship(back_populates="subject")
    related_subjects: list["SubjectRelation"] = Relationship(back_populates="subject")


# -------------------- 人物（Person）模型 --------------------
class Person(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    type: int  # 1: 个人, 2: 公司, 3: 组合
    career: str | None = Field(default=None, max_length=255)
    infobox: str | None = Field(default=None, max_length=1024)
    summary: str | None = Field(default=None, max_length=1024)
    comments: int = 0  # 评论/吐槽数
    collects: int = 0  # 收藏数

    # 人物与角色的关系
    characters: list["PersonCharacter"] = Relationship(back_populates="person")


# -------------------- 角色（Character）模型 --------------------
class Character(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    role: int  # 1: 角色, 2: 机体, 3: 组织, 4: 其他
    name: str = Field(max_length=255)
    infobox: str | None = Field(default=None, max_length=1024)
    summary: str | None = Field(default=None, max_length=1024)
    comments: int = 0  # 评论/吐槽数
    collects: int = 0  # 收藏数

    # 角色与人物的关系
    persons: list["PersonCharacter"] = Relationship(back_populates="character")

    # 角色与条目的关系
    subjects: list["SubjectCharacter"] = Relationship(back_populates="character")


# -------------------- 章节（Episode）模型 --------------------
class Episode(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    name_cn: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=1024)
    airdate: datetime | None = Field(default=None)
    disc: int | None = Field(default=None)
    duration: int | None = Field(default=None)  # 播放时长（分钟）
    subject_id: uuid.UUID = Field(foreign_key="subject.id")
    sort: int | None = Field(default=None)
    type: int  # 0: 正篇, 1: 特别篇, 2: OP, 3: ED, 4: Trailer, 5: MAD, 6: 其他

    # 关联的作品
    subject: Subject = Relationship(back_populates="episodes")


# -------------------- 条目与角色的关联（Subject-Characters）模型 --------------------
class SubjectCharacter(SQLModel, table=True):
    subject_id: uuid.UUID = Field(foreign_key="subject.id", primary_key=True)
    character_id: uuid.UUID = Field(foreign_key="character.id", primary_key=True)
    type: int  # 1: 主角, 2: 配角, 3: 客串等
    order: int  # 作品角色列表排序

    subject: Subject = Relationship(back_populates="characters")
    character: Character = Relationship(back_populates="subjects")


# -------------------- 条目与人物的关联（Subject-Persons）模型 --------------------
class SubjectPerson(SQLModel, table=True):
    person_id: uuid.UUID = Field(foreign_key="person.id", primary_key=True)
    subject_id: uuid.UUID = Field(foreign_key="subject.id", primary_key=True)
    position: str | None = Field(default=None, max_length=255)  # 人物担任的职位

    subject: Subject = Relationship(back_populates="persons")
    person: Person = Relationship(back_populates="subjects")


# -------------------- 人物与角色的关联（Person-Characters）模型 --------------------
class PersonCharacter(SQLModel, table=True):
    person_id: uuid.UUID = Field(foreign_key="person.id", primary_key=True)
    character_id: uuid.UUID = Field(foreign_key="character.id", primary_key=True)
    subject_id: uuid.UUID = Field(foreign_key="subject.id")
    summary: str | None = Field(default=None, max_length=1024)

    person: Person = Relationship(back_populates="characters")
    character: Character = Relationship(back_populates="persons")


# -------------------- 条目之间的关联（Subject-Relations）模型 --------------------
class SubjectRelation(SQLModel, table=True):
    subject_id: uuid.UUID = Field(foreign_key="subject.id", primary_key=True)
    relation_type: int  # 关联类型
    related_subject_id: uuid.UUID = Field(foreign_key="subject.id", primary_key=True)
    order: int  # 关联排序

    subject: Subject = Relationship(back_populates="related_subjects")


# 更新前向引用
Subject.update_forward_refs()
Person.update_forward_refs()
Character.update_forward_refs()
Episode.update_forward_refs()
