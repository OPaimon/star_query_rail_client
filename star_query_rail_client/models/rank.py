from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Rank")


@_attrs_define
class Rank:
    """Character rank.

    Attributes:
        id (int):
        pos (int):
        name (str):
        icon (str):
        desc (str):
        is_unlocked (bool):
    """

    id: int
    pos: int
    name: str
    icon: str
    desc: str
    is_unlocked: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        pos = self.pos

        name = self.name

        icon = self.icon

        desc = self.desc

        is_unlocked = self.is_unlocked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "pos": pos,
                "name": name,
                "icon": icon,
                "desc": desc,
                "is_unlocked": is_unlocked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        pos = d.pop("pos")

        name = d.pop("name")

        icon = d.pop("icon")

        desc = d.pop("desc")

        is_unlocked = d.pop("is_unlocked")

        rank = cls(
            id=id,
            pos=pos,
            name=name,
            icon=icon,
            desc=desc,
            is_unlocked=is_unlocked,
        )

        rank.additional_properties = d
        return rank

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
