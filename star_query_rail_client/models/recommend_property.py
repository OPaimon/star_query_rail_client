from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecommendProperty")


@_attrs_define
class RecommendProperty:
    """Recommend property.

    Attributes:
        id (int):
        recommend_relic_properties (List[int]):
        custom_relic_properties (List[int]):
        is_custom_property_valid (bool):
    """

    id: int
    recommend_relic_properties: List[int]
    custom_relic_properties: List[int]
    is_custom_property_valid: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        recommend_relic_properties = self.recommend_relic_properties

        custom_relic_properties = self.custom_relic_properties

        is_custom_property_valid = self.is_custom_property_valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "recommend_relic_properties": recommend_relic_properties,
                "custom_relic_properties": custom_relic_properties,
                "is_custom_property_valid": is_custom_property_valid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        recommend_relic_properties = cast(List[int], d.pop("recommend_relic_properties"))

        custom_relic_properties = cast(List[int], d.pop("custom_relic_properties"))

        is_custom_property_valid = d.pop("is_custom_property_valid")

        recommend_property = cls(
            id=id,
            recommend_relic_properties=recommend_relic_properties,
            custom_relic_properties=custom_relic_properties,
            is_custom_property_valid=is_custom_property_valid,
        )

        recommend_property.additional_properties = d
        return recommend_property

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
