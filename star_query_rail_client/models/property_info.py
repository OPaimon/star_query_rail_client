from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PropertyInfo")


@_attrs_define
class PropertyInfo:
    """Property info.

    Attributes:
        property_type (int):
        name (str):
        icon (str):
        property_name_relic (str):
        property_name_filter (str):
    """

    property_type: int
    name: str
    icon: str
    property_name_relic: str
    property_name_filter: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_type = self.property_type

        name = self.name

        icon = self.icon

        property_name_relic = self.property_name_relic

        property_name_filter = self.property_name_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_type": property_type,
                "name": name,
                "icon": icon,
                "property_name_relic": property_name_relic,
                "property_name_filter": property_name_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_type = d.pop("property_type")

        name = d.pop("name")

        icon = d.pop("icon")

        property_name_relic = d.pop("property_name_relic")

        property_name_filter = d.pop("property_name_filter")

        property_info = cls(
            property_type=property_type,
            name=name,
            icon=icon,
            property_name_relic=property_name_relic,
            property_name_filter=property_name_filter,
        )

        property_info.additional_properties = d
        return property_info

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
