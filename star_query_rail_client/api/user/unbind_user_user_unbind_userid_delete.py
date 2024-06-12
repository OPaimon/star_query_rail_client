from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    userid: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/user/unbind/{userid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Message]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Message.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Message]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    userid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, Message]]:
    """Unbind User

     Unbind user from account

    Args:
        userid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Message]]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    userid: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, Message]]:
    """Unbind User

     Unbind user from account

    Args:
        userid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Message]
    """

    return sync_detailed(
        userid=userid,
        client=client,
    ).parsed


async def asyncio_detailed(
    userid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, Message]]:
    """Unbind User

     Unbind user from account

    Args:
        userid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Message]]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    userid: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, Message]]:
    """Unbind User

     Unbind user from account

    Args:
        userid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Message]
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
        )
    ).parsed
