class Contract_Library:
    def __init__(self, session) -> None:
        self.session = session

    async def conteract_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Contract type related to ContractMaturity entity."""
        return await self.session.get(f"/contract/deps?masterid={master_id}")

    async def conteract_find(self, name: str) -> dict:
        """Retrieves an entity of Contract type by its name."""
        return await self.session.get(f"/contract/find?name={name}")

    async def contract_item(self, id: int) -> dict:
        """Retrieves an entity of Contract type by its id."""
        return await self.session.get(f"/contract/item?id={id}")

    async def contract_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Contract type by its ids."""
        return await self.session.get(f"/contract/items?ids={','.join([str(id) for id in ids])}")

    async def product_fee_params(self, product_ids: list[int]) -> dict:
        """Query the a product's fee parameters."""
        return await self.session.post(
            url="/contract/getproductfeeparams",
            payload={"productIds": [id for id in product_ids]},
        )

    async def contract_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Contract type related to multiple entities of ContractMaturity type."""
        return await self.session.get(f"/contract/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def roll_contract(self, name: str, forward: bool, ifExpired: bool) -> dict:
        """Request the best upcoming maturity date for a given contract."""
        return await self.session.post(
            url="/contract/rollcontract",
            payload={
                "name": name,
                "forward": forward,
                "ifExpired": ifExpired,
            },
        )

    async def contract_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Contract type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/contract/suggest?t={text}&l={n_entities}")

    async def contract_group_find(self, name: str) -> dict:
        """Retrieves an entity of ContractGroup type by its name."""
        return await self.session.get(f"/contractGroup/find?name={name}")

    async def contract_group_item(self, id: int) -> dict:
        """Retrieves an entity of ContractGroup type by its id."""
        return await self.session.get(f"/contractGroup/item?id={id}")

    async def contract_group_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ContractGroup type by its ids."""
        return await self.session.get(f"/contractGroup/items?ids={','.join([str(id) for id in ids])}")

    async def contract_group_list(self) -> dict:
        """Retrieves all entities of ContractGroup type."""
        return await self.session.get("/contractGroup/list")

    async def contract_group_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of ContractGroup type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/contractGroup/suggest?t={text}&l={n_entities}")

    async def contract_maturity_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of ContractMaturity type related to Product entity."""
        return await self.session.get(f"/ContractMaturity/deps?master_id={master_id}")

    async def contract_maturity_item(self, id: int) -> dict:
        """Retrieves an entity of ContractMaturity type by its id."""
        return await self.session.get(f"/ContractMaturity/item?id={id}")

    async def contract_maturity_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ContractMaturity type by its ids."""
        return await self.session.get(f"/ContractMaturity/items?ids={','.join([str(id) for id in ids])}")

    async def contract_maturity_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of ContractMaturity type related to multiple entities of Product type."""
        return await self.session.get(f"/contractMaturity/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def currency_find(self, name: str) -> dict:
        """Retrieves an entity of Currency type by its name."""
        return await self.session.get(f"/currency/find?name={name}")

    async def currency_item(self, id: int) -> dict:
        """Retrieves an entity of Currency type by its id."""
        return await self.session.get(f"/currency/item?id={id}")

    async def currency_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Currency type by its ids."""
        return await self.session.get(f"/currency/items?ids={','.join([str(id) for id in ids])}")

    async def currency_list(self) -> dict:
        """Retrieves all entities of Currency type."""
        return await self.session.get("/currency/list")

    async def currency_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Currency type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/currency/suggest?t={text}&l={n_entities}")

    async def currency_rate_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of CurrencyRate type related to Currency entity."""
        return await self.session.get(f"/currencyRate/deps?masterid={master_id}")

    async def currency_rate_item(self, id: int) -> dict:
        """Retrieves an entity of CurrencyRate type by its id."""
        return await self.session.get(f"/currencyRate/item?id={id}")

    async def currency_rate_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of CurrencyRate type by its ids."""
        return await self.session.get(f"/currencyRate/items?ids={','.join([str(id) for id in ids])}")

    async def currency_rate_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of CurrencyRate type related to multiple entities of Currency type."""
        return await self.session.get(f"/currencyRate/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def currency_rate_list(self) -> dict:
        """Retrieves all entities of CurrencyRate type."""
        return await self.session.get("/currencyRate/list")

    async def exchange_find(self, name: str) -> dict:
        """Retrieves an entity of Exchange type by its name."""
        return await self.session.get(f"/exchange/find?name={name}")

    async def exchange_item(self, id: int) -> dict:
        """Retrieves an entity of Exchange type by its id."""
        return await self.session.get(f"/exchange/item?id={id}")

    async def exchange_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Exchange type by its ids."""
        return await self.session.get(f"/exchange/items?ids={','.join([str(id) for id in ids])}")

    async def exchange_list(self) -> dict:
        """Retrieves all entities of Exchange type."""
        return await self.session.get("/exchange/list")

    async def exchange_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/exchange/suggest?t={text}&l={n_entities}")

    async def product_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Product type related to Exchange entity."""
        return await self.session.get(f"/product/deps?masterid={master_id}")

    async def product_find(self, name: str) -> dict:
        """Retrieves an entity of Product type by its name."""
        return await self.session.get(f"/product/find?name={name}")

    async def product_item(self, id: int) -> dict:
        """Retrieves an entity of Product type by its id."""
        return await self.session.get(f"/product/id={id}")

    async def product_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Product type by its ids."""
        return await self.session.get(f"/product/items?ids={','.join(str(id) for id in ids)}")

    async def product_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Product type related to multiple entities of Exchange type."""
        return await self.session.get(f"/product/ldeps?masterid={','.join([str(id) for id in master_ids])}")

    async def product_list(self) -> dict:
        """Retrieves all entities of Product type."""
        return await self.session.get("/product/list")

    async def product_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Product type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/product/suggest?t={text}&l={n_entities}")

    async def product_sess_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of ProductSession type related to Product entity."""
        return await self.session.get(f"/productSession/deps?masterid={master_id}")

    async def product_sess_item(self, id: int) -> dict:
        """Retrieves an entity of ProductSession type by its id."""
        return await self.session.get(f"/productSession/item?id={id}")

    async def product_session_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ProductSession type by its ids."""
        return await self.session.get(f"/productSession/items?ids={','.join([str(id) for id in ids])}")

    async def product_session_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of ProductSession type related to multiple entities of Product type."""
        return await self.session.get(f"/productSession/ldeps?masterids={','.join([str(id) for id in master_ids])}")

    async def spread_definition_item(self, id: int) -> dict:
        """Retrieves an entity of SpreadDefinition type by its id."""
        return await self.session.get(f"/SpreadDefinition/item?id={id}")

    async def spread_definition_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of SpreadDefinition type by its ids."""
        return await self.session.get(f"/SpreadDefinition/items?ids={','.join([str(id) for id in ids])}")
