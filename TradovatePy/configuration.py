class Configuration:

    def __init__(self, session) -> None:
        """Configuration Constructor"""
        self.session = session
        print(type(session))

    async def admin_alert_find(self, name: str) -> dict:
        """Retrieves an entity of AdminAlert type by its name."""
        return await self.session.get(f"/adminAlert/find?name={name}")

    async def admin_alert_item(self, id: int) -> dict:
        """Retrieves an entity of AdminAlert type by its id."""
        return await self.session.get(f"/adminAlert/item?id={id}")

    async def admin_alert_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of AdminAlert type by its ids."""
        return await self.session.get(
            f"/adminAlert/items?ids={','.join([str(id) for id in ids])}",
        )

    async def admin_alert_list(self) -> dict:
        """Retrieves all entities of AdminAlert type."""
        return await self.session.get("/adminAlert/list")

    async def admin_alert_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of AdminAlert type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/adminAlert/suggest?t={text}&l={n_entities}")

    async def clearing_house_find(self, name: str) -> dict:
        """Retrieves an entity of ClearingHouse type by its name."""
        return await self.session.get(f"/clearingHouse/find?name={name}")

    async def clearing_house_item(self, id: int) -> dict:
        """Retrieves an entity of ClearingHouse type by its id."""
        return await self.session.get(f"/clearingHouse/item?id={id}")

    async def clearing_house_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ClearingHouse type by its ids."""
        return await self.session.get(
            f"/clearingHouse/items?ids={','.join([str(id) for id in ids])}",
        )

    async def clearing_house_list(self) -> dict:
        """Retrieves all entities of ClearingHouse type."""
        return await self.session.get("/clearingHouse/list")

    async def clearing_house_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of ClearingHouse type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/clearingHouse/suggest?t={text}&l={n_entities}")

    async def entitlement_item(self, id: int) -> dict:
        """Retrieves an entity of Entitlement type by its id."""
        return await self.session.get(f"/entitlement/item?id={id}")

    async def entitlement_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Entitlement type by its ids."""
        return await self.session.get(f"/entitlement/items?ids={','.join([str(id) for id in ids])}")

    async def entitlement_list(self) -> dict:
        """Retrieves all entities of Entitlement type."""
        return await self.session.get("/entitlement/list")

    async def order_strategy_type_find(self, name: str) -> dict:
        """Retrieves an entity of OrderStrategyType type by its name."""
        return await self.session.get(f"/OrderStrategyType/find?name={name}")

    async def order_strategy_type_item(self, id: int) -> dict:
        """Retrieves an entity of OrderStrategyType type by its id."""
        return await self.session.get(f"/orderStrategyType/item?id={id}")

    async def order_strategy_type_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of OrderStrategyType type by its ids."""
        return await self.session.get(f"/orderStrategyType/items?ids={','.join([str(id) for id in ids])}")

    async def order_strategy_type_list(self) -> dict:
        """Retrieves all entities of OrderStrategyType type."""
        return await self.session.get("/orderStrategyType/list")

    async def order_strategy_type_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of OrderStrategyType type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/orderStrategyType/suggest?t={text}&l={n_entities}")

    async def property_find(self, name: str) -> dict:
        """Retrieves an entity of Property type by its name."""
        return await self.session.get(f"/property/find?name={name}")

    async def property_item(self, id: int) -> dict:
        """Retrieves an entity of Property type by its id."""
        return await self.session.get(f"/property/item?id={id}")

    async def property_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Property type by its ids."""
        return await self.session.get(
            f"/property/items?ids={','.join([str(id) for id in ids])}",
        )

    async def property_list(self) -> dict:
        """Retrieves all entities of Property type."""
        return await self.session.get("/property/list")

    async def property_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Property type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/property/suggest?t={text}&l={n_entities}")
