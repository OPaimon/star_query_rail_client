from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StarRailEquipment")


@_attrs_define
class StarRailEquipment:
    """Character equipment.

    Attributes:
        id (int):
        level (int):
        rank (int):
        name (str):
        desc (str):
        icon (str):
    """

    id: int
    level: int
    rank: int
    name: str
    desc: str
    icon: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        level = self.level

        rank = self.rank

        name = self.name

        desc = self.desc

        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "level": level,
                "rank": rank,
                "name": name,
                "desc": desc,
                "icon": icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        level = d.pop("level")

        rank = d.pop("rank")

        name = d.pop("name")

        desc = d.pop("desc")

        icon = d.pop("icon")

        star_rail_equipment = cls(
            id=id,
            level=level,
            rank=rank,
            name=name,
            desc=desc,
            icon=icon,
        )

        star_rail_equipment.additional_properties = d
        return star_rail_equipment

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
