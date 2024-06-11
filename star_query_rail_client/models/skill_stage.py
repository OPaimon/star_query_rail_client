from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SkillStage")


@_attrs_define
class SkillStage:
    """Character skill stage.

    Attributes:
        desc (str):
        name (str):
        level (int):
        remake (str):
        item_url (str):
        is_activated (bool):
        is_rank_work (bool):
    """

    desc: str
    name: str
    level: int
    remake: str
    item_url: str
    is_activated: bool
    is_rank_work: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc

        name = self.name

        level = self.level

        remake = self.remake

        item_url = self.item_url

        is_activated = self.is_activated

        is_rank_work = self.is_rank_work

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desc": desc,
                "name": name,
                "level": level,
                "remake": remake,
                "item_url": item_url,
                "is_activated": is_activated,
                "is_rank_work": is_rank_work,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desc = d.pop("desc")

        name = d.pop("name")

        level = d.pop("level")

        remake = d.pop("remake")

        item_url = d.pop("item_url")

        is_activated = d.pop("is_activated")

        is_rank_work = d.pop("is_rank_work")

        skill_stage = cls(
            desc=desc,
            name=name,
            level=level,
            remake=remake,
            item_url=item_url,
            is_activated=is_activated,
            is_rank_work=is_rank_work,
        )

        skill_stage.additional_properties = d
        return skill_stage

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
