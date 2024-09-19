from __future__ import annotations

from typing import TYPE_CHECKING

from realtime.types import RealtimeChannelOptions

if TYPE_CHECKING:
    from .client import SyncRealtimeClient


class SyncRealtimeChannel:
    """
    `Channel` is an abstraction for a topic listener for an existing socket connection.
    Each Channel has its own topic and a list of event-callbacks that responds to messages.
    Should only be instantiated through `connection.RealtimeClient().channel(topic)`.
    """

    def __init__(
        self,
        socket: SyncRealtimeClient,
        topic: str,
        params: RealtimeChannelOptions,
    ) -> None:
        """
        Initialize the Channel object.

        :param socket: RealtimeClient object
        :param topic: Topic that it subscribes to on the realtime server
        :param params: Optional parameters for connection.
        """
        raise NotImplementedError("This feature isn't available in the sync client."
                                  "You can use the realtime feature in the async client only.")