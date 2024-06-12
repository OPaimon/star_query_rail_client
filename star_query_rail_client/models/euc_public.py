from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.character_register import CharacterRegister


T = TypeVar("T", bound="EUCPublic")


@_attrs_define
class EUCPublic:
    """
    Attributes:
        email (str):
        userid (Union[Unset, int]):
        nickname (Union[Unset, str]):
        characters (Union[Unset, List['CharacterRegister']]):
    """

    email: str
    userid: Union[Unset, int] = UNSET
    nickname: Union[Unset, str] = UNSET
    characters: Union[Unset, List["CharacterRegister"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        userid = self.userid

        nickname = self.nickname

        characters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()
                characters.append(characters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if userid is not UNSET:
            field_dict["userid"] = userid
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.character_register import CharacterRegister

        d = src_dict.copy()
        email = d.pop("email")

        userid = d.pop("userid", UNSET)

        nickname = d.pop("nickname", UNSET)

        characters = []
        _characters = d.pop("characters", UNSET)
        for characters_item_data in _characters or []:
            characters_item = CharacterRegister.from_dict(characters_item_data)

            characters.append(characters_item)

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
