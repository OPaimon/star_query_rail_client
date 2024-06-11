from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EUCPublic")


@_attrs_define
class EUCPublic:
    """
    Attributes:
        email (str):
        userid (int):
        nickname (str):
        characters (List[int]):
    """

    email: str
    userid: int
    nickname: str
    characters: List[int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        userid = self.userid

        nickname = self.nickname

        characters = self.characters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "userid": userid,
                "nickname": nickname,
                "characters": characters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        userid = d.pop("userid")

        nickname = d.pop("nickname")

        characters = cast(List[int], d.pop("characters"))

        euc_public = cls(
            email=email,
            userid=userid,
            nickname=nickname,
            characters=characters,
        )

        euc_public.additional_properties = d
        return euc_public

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
