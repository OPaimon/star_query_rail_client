from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.equip_wiki import EquipWiki
    from ..models.property_info import PropertyInfo
    from ..models.recommend_property import RecommendProperty
    from ..models.relic_property import RelicProperty
    from ..models.star_rail_detail_character import StarRailDetailCharacter


T = TypeVar("T", bound="StarRailDetailCharacters")


@_attrs_define
class StarRailDetailCharacters:
    """StarRail characters.

    Attributes:
        avatar_list (List['StarRailDetailCharacter']):
        equip_wiki (List['EquipWiki']):
        property_info (List['PropertyInfo']):
        recommend_property (List['RecommendProperty']):
        relic_properties (List['RelicProperty']):
    """

    avatar_list: List["StarRailDetailCharacter"]
    equip_wiki: List["EquipWiki"]
    property_info: List["PropertyInfo"]
    recommend_property: List["RecommendProperty"]
    relic_properties: List["RelicProperty"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_list = []
        for avatar_list_item_data in self.avatar_list:
            avatar_list_item = avatar_list_item_data.to_dict()
            avatar_list.append(avatar_list_item)

        equip_wiki = []
        for equip_wiki_item_data in self.equip_wiki:
            equip_wiki_item = equip_wiki_item_data.to_dict()
            equip_wiki.append(equip_wiki_item)

        property_info = []
        for property_info_item_data in self.property_info:
            property_info_item = property_info_item_data.to_dict()
            property_info.append(property_info_item)

        recommend_property = []
        for recommend_property_item_data in self.recommend_property:
            recommend_property_item = recommend_property_item_data.to_dict()
            recommend_property.append(recommend_property_item)

        relic_properties = []
        for relic_properties_item_data in self.relic_properties:
            relic_properties_item = relic_properties_item_data.to_dict()
            relic_properties.append(relic_properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_list": avatar_list,
                "equip_wiki": equip_wiki,
                "property_info": property_info,
                "recommend_property": recommend_property,
                "relic_properties": relic_properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.equip_wiki import EquipWiki
        from ..models.property_info import PropertyInfo
        from ..models.recommend_property import RecommendProperty
        from ..models.relic_property import RelicProperty
        from ..models.star_rail_detail_character import StarRailDetailCharacter

        d = src_dict.copy()
        avatar_list = []
        _avatar_list = d.pop("avatar_list")
        for avatar_list_item_data in _avatar_list:
            avatar_list_item = StarRailDetailCharacter.from_dict(avatar_list_item_data)

            avatar_list.append(avatar_list_item)

        equip_wiki = []
        _equip_wiki = d.pop("equip_wiki")
        for equip_wiki_item_data in _equip_wiki:
            equip_wiki_item = EquipWiki.from_dict(equip_wiki_item_data)

            equip_wiki.append(equip_wiki_item)

        property_info = []
        _property_info = d.pop("property_info")
        for property_info_item_data in _property_info:
            property_info_item = PropertyInfo.from_dict(property_info_item_data)

            property_info.append(property_info_item)

        recommend_property = []
        _recommend_property = d.pop("recommend_property")
        for recommend_property_item_data in _recommend_property:
            recommend_property_item = RecommendProperty.from_dict(recommend_property_item_data)

            recommend_property.append(recommend_property_item)

        relic_properties = []
        _relic_properties = d.pop("relic_properties")
        for relic_properties_item_data in _relic_properties:
            relic_properties_item = RelicProperty.from_dict(relic_properties_item_data)

            relic_properties.append(relic_properties_item)

        star_rail_detail_characters = cls(
            avatar_list=avatar_list,
            equip_wiki=equip_wiki,
            property_info=property_info,
            recommend_property=recommend_property,
            relic_properties=relic_properties,
        )

        star_rail_detail_characters.additional_properties = d
        return star_rail_detail_characters

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
