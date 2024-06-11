from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.relic_prop import RelicProp


T = TypeVar("T", bound="Relic")


@_attrs_define
class Relic:
    """Character relic.

    Attributes:
        id (int):
        level (int):
        pos (int):
        name (str):
        desc (str):
        icon (str):
        rarity (int):
        main_property (RelicProp): Character relic property.
        properties (List['RelicProp']):
    """

    id: int
    level: int
    pos: int
    name: str
    desc: str
    icon: str
    rarity: int
    main_property: "RelicProp"
    properties: List["RelicProp"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        level = self.level

        pos = self.pos

        name = self.name

        desc = self.desc

        icon = self.icon

        rarity = self.rarity

        main_property = self.main_property.to_dict()

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "level": level,
                "pos": pos,
                "name": name,
                "desc": desc,
                "icon": icon,
                "rarity": rarity,
                "main_property": main_property,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relic_prop import RelicProp

        d = src_dict.copy()
        id = d.pop("id")

        level = d.pop("level")

        pos = d.pop("pos")

        name = d.pop("name")

        desc = d.pop("desc")

        icon = d.pop("icon")

        rarity = d.pop("rarity")

        main_property = RelicProp.from_dict(d.pop("main_property"))

        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = RelicProp.from_dict(properties_item_data)

            properties.append(properties_item)

        relic = cls(
            id=id,
            level=level,
            pos=pos,
            name=name,
            desc=desc,
            icon=icon,
            rarity=rarity,
            main_property=main_property,
            properties=properties,
        )

        relic.additional_properties = d
        return relic

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
