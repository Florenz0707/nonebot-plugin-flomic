from pydantic import BaseModel
from nonebot import get_plugin_config


class Config(BaseModel):
    jm_username: str = ""
    jm_password: str = ""
    threading_image: int = 20
    threading_photo: int = 15


jm_config = get_plugin_config(Config)
