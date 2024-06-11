from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.skill_stage import SkillStage


T = TypeVar("T", bound="Skill")


@_attrs_define
class Skill:
    """Character skill.

    Attributes:
        point_id (int):
        point_type (int):
        item_url (str):
        level (int):
        is_activated (bool):
        is_rank_work (bool):
        pre_point (int):
        anchor (str):
        remake (str):
        skill_stages (List['SkillStage']):
    """

    point_id: int
    point_type: int
    item_url: str
    level: int
    is_activated: bool
    is_rank_work: bool
    pre_point: int
    anchor: str
    remake: str
    skill_stages: List["SkillStage"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        point_id = self.point_id

        point_type = self.point_type

        item_url = self.item_url

        level = self.level

        is_activated = self.is_activated

        is_rank_work = self.is_rank_work

        pre_point = self.pre_point

        anchor = self.anchor

        remake = self.remake

        skill_stages = []
        for skill_stages_item_data in self.skill_stages:
            skill_stages_item = skill_stages_item_data.to_dict()
            skill_stages.append(skill_stages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "point_id": point_id,
                "point_type": point_type,
                "item_url": item_url,
                "level": level,
                "is_activated": is_activated,
                "is_rank_work": is_rank_work,
                "pre_point": pre_point,
                "anchor": anchor,
                "remake": remake,
                "skill_stages": skill_stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.skill_stage import SkillStage

        d = src_dict.copy()
        point_id = d.pop("point_id")

        point_type = d.pop("point_type")

        item_url = d.pop("item_url")

        level = d.pop("level")

        is_activated = d.pop("is_activated")

        is_rank_work = d.pop("is_rank_work")

        pre_point = d.pop("pre_point")

        anchor = d.pop("anchor")

        remake = d.pop("remake")

        skill_stages = []
        _skill_stages = d.pop("skill_stages")
        for skill_stages_item_data in _skill_stages:
            skill_stages_item = SkillStage.from_dict(skill_stages_item_data)

            skill_stages.append(skill_stages_item)

        skill = cls(
            point_id=point_id,
            point_type=point_type,
            item_url=item_url,
            level=level,
            is_activated=is_activated,
            is_rank_work=is_rank_work,
            pre_point=pre_point,
            anchor=anchor,
            remake=remake,
            skill_stages=skill_stages,
        )

        skill.additional_properties = d
        return skill

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
