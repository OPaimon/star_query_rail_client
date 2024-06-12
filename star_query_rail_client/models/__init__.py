"""Contains all the data models used in inputs/outputs"""

from .body_login_access_token_login_access_token_post import BodyLoginAccessTokenLoginAccessTokenPost
from .character_prop import CharacterProp
from .character_register import CharacterRegister
from .connect_uc_register import ConnectUCRegister
from .email import Email
from .email_base import EmailBase
from .email_register import EmailRegister
from .email_update import EmailUpdate
from .equip_wiki import EquipWiki
from .euc_public import EUCPublic
from .http_validation_error import HTTPValidationError
from .message import Message
from .property_info import PropertyInfo
from .rank import Rank
from .recommend_property import RecommendProperty
from .relic import Relic
from .relic_prop import RelicProp
from .relic_property import RelicProperty
from .skill import Skill
from .skill_stage import SkillStage
from .star_rail_detail_character import StarRailDetailCharacter
from .star_rail_detail_characters import StarRailDetailCharacters
from .star_rail_equipment import StarRailEquipment
from .token import Token
from .user_create import UserCreate
from .user_test import UserTest
from .validation_error import ValidationError

__all__ = (
    "BodyLoginAccessTokenLoginAccessTokenPost",
    "CharacterProp",
    "CharacterRegister",
    "ConnectUCRegister",
    "Email",
    "EmailBase",
    "EmailRegister",
    "EmailUpdate",
    "EquipWiki",
    "EUCPublic",
    "HTTPValidationError",
    "Message",
    "PropertyInfo",
    "Rank",
    "RecommendProperty",
    "Relic",
    "RelicProp",
    "RelicProperty",
    "Skill",
    "SkillStage",
    "StarRailDetailCharacter",
    "StarRailDetailCharacters",
    "StarRailEquipment",
    "Token",
    "UserCreate",
    "UserTest",
    "ValidationError",
)
