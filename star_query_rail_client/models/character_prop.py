from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CharacterProp")


@_attrs_define
class CharacterProp:
    """Character property.

    Attributes:
        property_type (int):
        base (str):
        add (str):
        final (str):
    """

    property_type: int
    base: str
    add: str
    final: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_type = self.property_type

        base = self.base

        add = self.add

        final = self.final

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_type": property_type,
                "base": base,
                "add": add,
                "final": final,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_type = d.pop("property_type")

        base = d.pop("base")

        add = d.pop("add")

        final = d.pop("final")

        character_prop = cls(
            property_type=property_type,
            base=base,
            add=add,
            final=final,
        )

        character_prop.additional_properties = d
        return character_prop

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
