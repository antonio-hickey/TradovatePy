class Alerts:
    """Class of methods related to alerts."""

    def __init__(self, session) -> None:
        """Alerts constructor."""
        self.session = session

    async def complete_alert_signal(self, admin_alert_signal_id: int) -> dict:
        """An "Incomplete" notification is one that has not yet been viewed by a user.
           Once a user has interacted with a notification it should be "completed"."""
        return await self.session.post(
            url="/adminAlertSignal/completealertsignal",
            payload={"adminAlertSignalId": admin_alert_signal_id},
        )

    async def admin_alert_signal_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of AdminAlertSignal type related to AdminAlert entity."""
        return await self.session.get(f"/adminAlertSignal/deps?master_id={master_id}")

    async def admin_alert_signal_item(self, id: int) -> dict:
        """Retrieves an entity of AdminAlertSignal type by its id."""
        return await self.session.get(f"/adminAlertSignal/item?id={id}")

    async def admin_alert_signal_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of AdminAlertSignal type by its ids."""
        return await self.session.get(f"/adminAlertSignal/items?ids={','.join([str(id) for id in ids])}")

    async def admin_alert_signal_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of AdminAlertSignal type related to multiple entities of AdminAlert type."""
        return await self.session.get(f"/adminAlertSignal/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def admin_alert_signal_list(self) -> dict:
        """Retrieves all entities of AdminAlertSignal type."""
        return await self.session.get("/adminAlertSignal/list")

    async def take_alert_signal_ownership(self, admin_alert_signal_id: int) -> dict:
        """Internal. Can be used by B2B partners to mark an adminAlertSignal entity for further handling."""
        return await self.session.post(
            url="/adminAlertSignal/takealertsignalownership",
            payload={"adminAlertSignalId": admin_alert_signal_id},
        )

    async def create_alert(self,
                           expression: str,
                           valid_until: str,
                           trigger_limits: int,
                           message: str) -> dict:
        """Create an alert entity associated with the user."""
        return await self.session.post(
            url="/alert/createalert",
            payload={
                "expression": expression,
                "validUntil": valid_until,
                "triggerLimits": trigger_limits,
                "message": message,
            },
        )

    async def delete_alert(self, alert_id: int) -> dict:
        """Remove an alert entity associated with the user."""
        return await self.session.post(
            url="/alert/deletealert",
            payload={"alertId": alert_id},
        )

    async def alert_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Alert type related to User entity."""
        return await self.session.get(f"/alert/deps?master_id={master_id}")

    async def dismiss_alert(self, alert_id: int) -> dict:
        """Dismiss an alert for a user."""
        return await self.session.post(
            url="/alert/dismissalert",
            payload={"alertId": alert_id},
        )

    async def alert_item(self, id: int) -> dict:
        """Retrieves an entity of Alert type by its id."""
        return await self.session.get(f"/alert/item?id={id}")

    async def alert_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Alert type by its ids."""
        return await self.session.get(f"/alert/items?ids={','.join([str(id) for id in ids])}")

    async def alert_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Alert type related to multiple entities of User type."""
        return await self.session.get(f"/alert/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def alert_list(self) -> dict:
        """Retrieves all entities of Alert type."""
        return await self.session.get("/alert/list")

    async def mark_read_alert_signal(self, alert_id: int, alert_signal_id: int) -> dict:
        """Mark an alert entity as 'read' for a user."""
        return await self.session.post(
            url="/alert/markreadalertsignal",
            payload={
                "alertId": alert_id,
                "alertSignalId": alert_signal_id,
            },
        )

    async def modify_alert(self,
                           alert_id: int,
                           expression: str,
                           valid_until: str = None,
                           trigger_limits: int = None,
                           message: str = "") -> dict:
        """Change the parameters of an existing alert."""
        payload = {
            "alertId": alert_id,
            "expression": expression,
        }
        if valid_until is not None:
            payload["validUntil"] = valid_until
        if trigger_limits is not None:
            payload["triggerLimits"] = trigger_limits
        if message is not None:
            payload["message"] = message

        return await self.session.post(
            url="/alert/modifyalert",
            payload=payload,
        )

    async def reset_alert(self, alert_id: int) -> dict:
        """
            Resets an alert.
            You can use this method after an alert has been triggered
            to keep the alert and wait for the alert to be triggered again.
        """
        return await self.session.post(
            url="/alert/resetalert",
            payload={"alertId": alert_id},
        )

    async def alert_signal_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of AlertSignal type related to Alert entity."""
        return await self.session.get(f"/alertSignal/deps?masterid={master_id}")

    async def alert_signal_item(self, id: int) -> dict:
        """Retrieves an entity of AlertSignal type by its id."""
        return await self.session.get(f"/alertSignal/item?id={id}")

    async def alert_signal_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of AlertSignal type by its ids."""
        return await self.session.get(f"/alertSignal/items?ids={','.join([str(id) for id in ids])}")

    async def alert_signal_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of AlertSignal type related to multiple entities of Alert type."""
        return await self.session.get(f"/alertSignal/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def alert_signal_list(self) -> dict:
        """Retrieves all entities of AlertSignal type."""
        return await self.session.get("/alertSignal/list")
