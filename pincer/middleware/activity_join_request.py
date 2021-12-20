# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the user receives a Rich Presence Ask to Join request"""

from __future__ import annotations

from ..objects.user.user import User
from ..utils.conversion import construct_client_dict
from ..utils.types import Coro

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Dispatcher
    from ..core.dispatch import GatewayDispatch


async def activity_join_request_middleware(
    self: Client,
    gateway: Dispatcher,
    payload: GatewayDispatch
):
    """|coro|

    Middleware for the ``on_activity_join_request`` event.

    Parameters
    ----------
    payload : :class:`~pincer.core.gateway.GatewayDispatch`
        The data received from the activity join request event.

    Returns
    -------
    Tuple[:class:`str`, :class:`~pincer.objects.user.user.User`]
        ``on_activity_join_request`` and a ``User``
    """
    return (
        "on_activity_join_request",
        User.from_dict(construct_client_dict(self, payload.data)),
    )


def export() -> Coro:
    return activity_join_request_middleware
