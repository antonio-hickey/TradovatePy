class Accounting:

    def __init__(self, session) -> None:
        """Accounting constructor"""
        self.session = session

    async def account_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Account type related to User entity."""
        return await self.session.get(f"/account/deps?masterid={master_id}")

    async def account_find(self, name: str) -> dict:
        """Retrieves an entity of Account type by its name."""
        return await self.session.get(f"/account/find?name={name}")

    async def account_item(self, id: int) -> dict:
        """Retrieves an entity of Account type by its id."""
        return await self.session.get(f"/account/item?id={id}")

    async def account_items(self, ids: list[int]) -> dict:
        """Retrieves an entity of Account type by its ids."""
        return await self.session.get(f"/account/items?ids={','.join([str(id) for id in ids])}")

    async def account_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Account type related to multiple entities of User type"""
        return await self.session.get(f"/account/deps?masterid={','.join([str(id) for id in master_ids])}")

    async def account_list(self) -> dict:
        """Retrieves all entities of Account type."""
        return await self.session.get("/account/list")

    async def account_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Account type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/account/suggest?t={text}&l={n_entities}")

    async def cash_balance_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of CashBalance type related to Account entity."""
        return await self.session.get(f"/cashBalance/deps?masterid={master_id}")

    async def cash_balance_snapshot(self, account_id: int) -> dict:
        """Get a snapshot of an account's current cash balance."""
        return await self.session.post(
            url="/cashBalance/getcashbalancesnapshot",
            payload={"accountId": account_id},
        )

    async def cash_balance_item(self, id: int) -> dict:
        """Retrieves an entity of CashBalance type by its id."""
        return await self.session.get(f"/cashBalance/item?id={id}")

    async def cash_balance_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of CashBalance type by its ids."""
        return await self.session.get(f"/cashBalance/items?ids={','.join([str(id) for id in ids])}")

    async def cash_balance_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of CashBalance type related to multiple entities of Account type."""
        return await self.session.get(f"/cashBalance/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def cash_balance_list(self) -> dict:
        """Retrieves all entities of CashBalance type."""
        return await self.session.get("/cashBalance/list")

    async def cash_balance_log_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of CashBalanceLog type related to Account entity."""
        return await self.session.get(f"/cashBalanceLog/deps?masterid={master_id}")

    async def cash_balance_log_item(self, id: int) -> dict:
        """Retrieves an entity of CashBalanceLog type by its id."""
        return await self.session.get(f"/cashBalanceLog/item?id={id}")

    async def cash_balance_log_items(self, ids: list[int]) -> dict:
        """Retrieves an entity of CashBalanceLog type by its id."""
        return await self.session.get(f"/cashBalanceLog/item?ids={','.join(str(id) for id in ids)}")

    async def cash_balance_log_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of CashBalanceLog type related to multiple entities of Account type."""
        return await self.session.get(f"/cashBalanceLog/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def margin_snapshot_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of MarginSnapshot type related to Account entity."""
        return await self.session.get(f"/marginSnapshot/deps?masterid={master_id}")

    async def margin_snapshot_item(self, id: int) -> dict:
        """Retrieves an entity of MarginSnapshot type by its id."""
        return await self.session.get(f"/marginSnapshot/item?id={id}")

    async def margin_snapshot_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of MarginSnapshot type by its ids."""
        return await self.session.get(f"/marginSnapshot/items?ids={','.join(str(id) for id in ids)}")

    async def margin_snapshot_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of MarginSnapshot type related to multiple entities of Account type."""
        return await self.session.get(f"/marginSnapshot/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def margin_snapshot_list(self) -> dict:
        """Retrieves all entities of MarginSnapshot type."""
        return await self.session.get("/marginSnapshot/list")

    async def permission_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of TradingPermission type related to User entity."""
        return await self.session.get(f"/tradingPermission/deps?masterid={master_id}")

    async def permission_item(self, id: int) -> dict:
        """Retrieves an entity of TradingPermission type by its id."""
        return await self.session.get(f"/tradingPermission/item?id={id}")

    async def permission_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of TradingPermission type by its ids."""
        return await self.session.get(f"/tradingPermission/items?ids={','.join([str(id) for id in ids])}")

    async def permission_L_Dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of TradingPermission type related to multiple entities of User type."""
        return await self.session.get(f"/tradingPermission/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def permission_list(self) -> dict:
        """Retrieves all entities of TradingPermission type."""
        return await self.session.get("/tradingPermission/list")
