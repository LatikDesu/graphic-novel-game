import sqlalchemy

metadata = sqlalchemy.MetaData()

scene_table = sqlalchemy.Table(
    "scene",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("path_img", sqlalchemy.String(100)),
)

window_table = sqlalchemy.Table(
    "window",
    metadata,
    sqlalchemy.Column("window_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("scene_id", sqlalchemy.ForeignKey("scene.id")),
    sqlalchemy.Column("text", sqlalchemy.String(100)),
    sqlalchemy.Column("character", sqlalchemy.String(100)),
    sqlalchemy.Column("path_img", sqlalchemy.String(100)),
    sqlalchemy.Column("position", sqlalchemy.String(100)),
)
