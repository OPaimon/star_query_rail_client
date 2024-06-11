from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RelicProperty")


@_attrs_define
class RelicProperty:
    """Relic property.

    Attributes:
        property_type (int):
        modify_property_type (int):
    """

    property_type: int
    modify_property_type: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_type = self.property_type

        modify_property_type = self.modify_property_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_type": property_type,
                "modify_property_type": modify_property_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_type = d.pop("property_type")

        modify_property_type = d.pop("modify_property_type")

        relic_property = cls(
            property_type=property_type,
            modify_property_type=modify_property_type,
        )

        relic_property.additional_properties = d
        return relic_property

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
