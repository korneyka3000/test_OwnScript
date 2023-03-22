import enum


@enum.unique
class Colors(enum.Enum):
    """Возможные цвета свечения для фонаря"""
    white: str = "white"
    blue: str = "blue"
    red: str = "red"
    yellow: str = "yellow"

    @classmethod
    def get_default_color(cls):
        return tuple(cls._member_map_.values())[0].value

    @classmethod
    def members_dict(cls):
        return cls._member_map_

    @classmethod
    def members_list(cls):
        return cls._member_names_
