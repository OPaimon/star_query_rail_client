from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.character_prop import CharacterProp
    from ..models.rank import Rank
    from ..models.relic import Relic
    from ..models.skill import Skill
    from ..models.star_rail_equipment import StarRailEquipment


T = TypeVar("T", bound="StarRailDetailCharacter")


@_attrs_define
class StarRailDetailCharacter:
    """StarRail character with equipment and relics.

    Attributes:
        id (int):
        element (str):
        rarity (int):
        icon (str):
        name (str):
        level (int):
        rank (int):
        image (str):
        relics (List['Relic']):
        ornaments (List['Relic']):
        ranks (List['Rank']):
        properties (List['CharacterProp']):
        skills (List['Skill']):
        base_type (int):
        figure_path (str):
        equip (Union[Unset, StarRailEquipment]): Character equipment.
    """

    id: int
    element: str
    rarity: int
    icon: str
    name: str
    level: int
    rank: int
    image: str
    relics: List["Relic"]
    ornaments: List["Relic"]
    ranks: List["Rank"]
    properties: List["CharacterProp"]
    skills: List["Skill"]
    base_type: int
    figure_path: str
    equip: Union[Unset, "StarRailEquipment"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        element = self.element

        rarity = self.rarity

        icon = self.icon

        name = self.name

        level = self.level

        rank = self.rank

        image = self.image

        relics = []
        for relics_item_data in self.relics:
            relics_item = relics_item_data.to_dict()
            relics.append(relics_item)

        ornaments = []
        for ornaments_item_data in self.ornaments:
            ornaments_item = ornaments_item_data.to_dict()
            ornaments.append(ornaments_item)

        ranks = []
        for ranks_item_data in self.ranks:
            ranks_item = ranks_item_data.to_dict()
            ranks.append(ranks_item)

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        skills = []
        for skills_item_data in self.skills:
            skills_item = skills_item_data.to_dict()
            skills.append(skills_item)

        base_type = self.base_type

        figure_path = self.figure_path

        equip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equip, Unset):
            equip = self.equip.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "element": element,
                "rarity": rarity,
                "icon": icon,
                "name": name,
                "level": level,
                "rank": rank,
                "image": image,
                "relics": relics,
                "ornaments": ornaments,
                "ranks": ranks,
                "properties": properties,
                "skills": skills,
                "base_type": base_type,
                "figure_path": figure_path,
            }
        )
        if equip is not UNSET:
            field_dict["equip"] = equip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.character_prop import CharacterProp
        from ..models.rank import Rank
        from ..models.relic import Relic
        from ..models.skill import Skill
        from ..models.star_rail_equipment import StarRailEquipment

        d = src_dict.copy()
        id = d.pop("id")

        element = d.pop("element")

        rarity = d.pop("rarity")

        icon = d.pop("icon")

        name = d.pop("name")

        level = d.pop("level")

        rank = d.pop("rank")

        image = d.pop("image")

        relics = []
        _relics = d.pop("relics")
        for relics_item_data in _relics:
            relics_item = Relic.from_dict(relics_item_data)

            relics.append(relics_item)

        ornaments = []
        _ornaments = d.pop("ornaments")
        for ornaments_item_data in _ornaments:
            ornaments_item = Relic.from_dict(ornaments_item_data)

            ornaments.append(ornaments_item)

        ranks = []
        _ranks = d.pop("ranks")
        for ranks_item_data in _ranks:
            ranks_item = Rank.from_dict(ranks_item_data)

            ranks.append(ranks_item)

        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = CharacterProp.from_dict(properties_item_data)

            properties.append(properties_item)

        skills = []
        _skills = d.pop("skills")
        for skills_item_data in _skills:
            skills_item = Skill.from_dict(skills_item_data)

            skills.append(skills_item)

        base_type = d.pop("base_type")

        figure_path = d.pop("figure_path")

        _equip = d.pop("equip", UNSET)
        equip: Union[Unset, StarRailEquipment]
        if isinstance(_equip, Unset):
            equip = UNSET
        else:
            equip = StarRailEquipment.from_dict(_equip)

        star_rail_detail_character = cls(
            id=id,
            element=element,
            rarity=rarity,
            icon=icon,
            name=name,
            level=level,
            rank=rank,
            image=image,
            relics=relics,
            ornaments=ornaments,
            ranks=ranks,
            properties=properties,
            skills=skills,
            base_type=base_type,
            figure_path=figure_path,
            equip=equip,
        )

        star_rail_detail_character.additional_properties = d
        return star_rail_detail_character

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
