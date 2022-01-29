class Positions:
    def __init__(self, session) -> None:
        self.session = session

    async def fill_pair_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of FillPair type related to Position entity."""
        return await self.session.get(f"fillPair/deps?id={master_id}")

    async def fill_pair_item(self, id: int) -> dict:
        """Retrieves an entity of FillPair type by its id."""
        return await self.session.get(f"/fillPair/item?id={id}")

    async def fill_pair_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of FillPair type by its ids."""
        return await self.session.get(f"/fillPair/items?ids{','.join([str(id) for id in ids])}")

    async def fill_pair_l_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of FillPair type related to multiple entities of Position type."""
        return await self.session.get(f"/fillPair/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def fill_pair_list(self) -> dict:
        """Retrieves all entities of FillPair type."""
        return await self.session.get("/fillPair/list")

    async def position_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Position type related to Account entity."""
        return await self.session.get(f"/postion/deps?masterid={master_id}")

    async def position_find(self, name: str) -> dict:
        """Retrieves an entity of Position type by its name."""
        return await self.session.get(f"/position/find?name={name}")

    async def position_item(self, id: int) -> dict:
        """Retrieves an entity of Position type by its id."""
        return await self.session.get(f"/position/item?id={id}")

    async def position_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Position type by its ids."""
        return await self.session.get(f"/position/items?ids={','.join([str(id) for id in ids])}")

    async def position_l_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Position type related to multiple entities of Account type."""
        return await self.session.get(f"/postion/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def position_list(self) -> dict:
        """Retrieves all entities of Position type."""
        return await self.session.get("/position/list")
