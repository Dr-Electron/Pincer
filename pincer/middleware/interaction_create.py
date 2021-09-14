# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Pincer
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from pincer.commands import ChatCommandHandler
from pincer.core.dispatch import GatewayDispatch
from pincer.objects import Interaction, Embed, Message, InteractionFlags
from pincer.utils import MISSING, should_pass_cls, Coro
from pincer.utils.extraction import get_params


async def interaction_create_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_interaction``, which handles command
    execution.

    :param self:
        The current client.

    :param payload:
        The data received from the interaction event.
    """
    interaction: Interaction = Interaction.from_dict(payload.data)
    command = ChatCommandHandler.register.get(interaction.data.name)

    if command:
        defaults = {param: None for param in get_params(command.call)}
        params = {}

        if interaction.data.options is not MISSING:
            params = {
                opt.name: opt.value for opt in interaction.data.options
            }

        kwargs = {**defaults, **params}

        if should_pass_cls(command.call):
            kwargs["self"] = self

        message = await command.call(**kwargs)

        if isinstance(message, Embed):
            message = Message(embeds=[message])
        elif not isinstance(message, Message):
            message = Message(message) if message else Message(
                self.__received,
                flags=InteractionFlags.EPHEMERAL
            )

        await self.http.post(
            f"interactions/{interaction.id}/{interaction.token}/callback",
            message.to_dict()
        )

    return "on_interaction_create", [interaction]


def export() -> Coro:
    return interaction_create_middleware
