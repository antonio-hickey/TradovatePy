class Orders:
    """Class of methods related to orders."""

    def __init__(self, session) -> None:
        self.session = session

    async def command_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Command type related to Order entity."""
        return await self.session.get(f"/command/deps?masterid={master_id}")

    async def command_item(self, id: int) -> dict:
        """Retrieves an entity of Command type by its id."""
        return await self.session.get(f"/command/item?id={id}")

    async def command_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Command type by its ids."""
        return await self.session.get(
            f"/command/items?ids={','.join([str(id) for id in ids])}",
        )

    async def command_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Command type related to multiple entities of Order type."""
        return await self.session.get(
            f"/command/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def command_list(self) -> dict:
        """Retrieves all entities of Command type."""
        return await self.session.get("/command/list")

    async def command_report_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of CommandReport type related to Command entity."""
        return await self.session.get(f"/commandReport/deps?masterid={master_id}")

    async def command_report_item(self, id: int) -> dict:
        """Retrieves an entity of CommandReport type by its id."""
        return await self.session.get(f"/commandReport/item?id={id}")

    async def command_report_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of CommandReport type by its ids."""
        return await self.session.get(
            f"/commandReport/items?ids={','.join([str(id) for id in ids])}",
        )

    async def command_report_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of CommandReport type related to multiple entities of Command type."""
        return await self.session.get(
            f"/commandReport/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def command_report_list(self) -> dict:
        """Retrieves all entities of CommandReport type."""
        return await self.session.get("/commandReport/list")

    async def execution_report_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of ExecutionReport type related to Command entity."""
        return await self.session.get(f"/executionReport/deps?masterid={master_id}")

    async def execution_report_find(self, name: str) -> dict:
        """Retrieves an entity of ExecutionReport type by its name."""
        return await self.session.get(f"/executionReport/find?name={name}")

    async def execution_report_item(self, id: int) -> dict:
        """Retrieves an entity of ExecutionReport type by its id."""
        return await self.session.get(f"/executionReport/item?id={id}")

    async def execution_report_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ExecutionReport type by its ids."""
        return await self.session.get(
            f"/executionReport/items?ids={','.join([str(id) for id in ids])}",
        )

    async def execution_report_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of ExecutionReport type related to multiple entities of Command type."""
        return await self.session.get(
            f"/executionReport/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def execution_report_list(self) -> dict:
        """Retrieves all entities of ExecutionReport type."""
        return await self.session.get("/executionReport/list")

    async def execution_report_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of ExecutionReport type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/executionReport/suggest?t={text}&l={n_entities}")

    async def fill_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Fill type related to Order entity."""
        return await self.session.get(f"/fill/deps?masterid={master_id}")

    async def fill_item(self, id: int) -> dict:
        """Retrieves an entity of Fill type by its id."""
        return await self.session.get(f"/fill/item?id={id}")

    async def fill_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Fill type by its ids."""
        return await self.session.get(
            f"/fill/items?ids={','.join([str(id) for id in ids])}",
        )

    async def fill_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Fill type related to multiple entities of Order type."""
        return await self.session.get(
            f"/fill/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def fill_list(self) -> dict:
        """Retrieves all entities of Fill type."""
        return await self.session.get("/fill/list")

    async def fill_fee_dependent(self, master_id: int) -> dict:
        """Retrieves all entities of FillFee type related to Fill entity."""
        return await self.session.get(f"/fillFee/deps?masterid={master_id}")

    async def fill_fee_item(self, id: int) -> dict:
        """Retrieves an entity of FillFee type by its id."""
        return await self.session.get(f"/fillFee/item?id={id}")

    async def fill_fee_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of FillFee type by its ids."""
        return await self.session.get(
            f"/fillFee/items?ids={','.join([str(id) for id in ids])}",
        )

    async def fill_fee_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of FillFee type related to multiple entities of Fill type."""
        return await self.session.get(
            f"/fillFee/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def fill_fee_list(self) -> dict:
        """Retrieves all entities of FillFee type."""
        return self.session.get("/fillFee/list")

    async def cancel_order(self,
                           order_id: int,
                           cl_ord_id: str = None,
                           activation_time: str = None,
                           custom_tag_50: str = None,
                           is_automated: bool = None) -> dict:
        """Make a request to cancel an order."""
        return await self.session.post(
            url="/order/cancelorder",
            payload={
                "orderId": order_id,
                "clOrdId": cl_ord_id,
                "activationTime": activation_time,
                "customTag50": custom_tag_50,
                "isAutomated": is_automated,
            },
        )

    async def order_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of Order type related to Account entity."""
        return await self.session.get(f"/order/deps?masterid={master_id}")

    async def order_item(self, id: int) -> dict:
        """Retrieves an entity of Order type by its id."""
        return await self.session.get(f"/order/item?id={id}")

    async def order_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Order type by its ids."""
        return await self.session.get(
            f"/order/items?ids={','.join([str(id) for id in ids])}",
        )

    async def order_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of Order type related to multiple entities of Account type."""
        return await self.session.get(
            f"/order/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def liquidate_position(self,
                                 account_id: int,
                                 contract_id: int,
                                 admin: bool,
                                 custom_tag_50: str = None) -> dict:
        """
        Send a request to cancel orders for a specific contract and close that position for the given account.
        This request initiates the cancellation process of open orders for an existing position held by this account.

        Note: This is a request to cancel orders and close a position, not a guarantee.
              Any operation could fail for a number of reasons, ranging from Exchange
              rejection to incorrect parameterization.
        """
        return await self.session.post(
            url="/order/liquidateposition",
            payload={
                "accountId": account_id, "contractId": contract_id,
                "admin": admin, "customTag50": custom_tag_50,
            },
        )

    async def order_list(self) -> dict:
        """Retrieves all entities of Order type."""
        return await self.session.get("/order/limit")

    async def modify_order(self,
                           order_id: int,
                           order_qty: int,
                           order_type: str,
                           cl_ord_id: str = None,
                           price: float = None,
                           stop_price: float = None,
                           max_show: int = None,
                           peg_difference: float = None,
                           time_in_force: str = None,
                           expire_time: str = None,
                           text: str = None,
                           activation_time: str = None,
                           custom_tag_50: str = None,
                           is_automated: bool = None) -> dict:
        """
        Make a request to modify the parameters of an order.
        You can request changes to an order, such as the trigger price for a Stop or Limit order.

        Note: This is no guarantee that the order can be modified in a given way.
              Market and exchange rules apply.
        """
        return await self.session.post(
            url="/order/modifyorder",
            payload={
                "orderId": order_id, "clOrdId": cl_ord_id,
                "orderQty": order_qty, "orderType": order_type,
                "price": price, "stopPrice": stop_price,
                "maxShow": max_show, "pegDifference": peg_difference,
                "timeInForce": time_in_force, "expireTime": expire_time,
                "text": text, "activationTime": activation_time,
                "customTag50": custom_tag_50, "isAutomated": is_automated,
            },
        )

    async def place_OCO(self,
                        action: str,
                        symbol: str,
                        order_qty: int,
                        order_type: str,
                        other_action: str,
                        other_order_type: str,
                        account_spec: str = None,
                        account_id: int = None,
                        cl_ord_id: str = None,
                        price: float = None,
                        stop_price: float = None,
                        max_show: int = None,
                        peg_difference: float = None,
                        time_in_force: str = None,
                        expire_time: str = None,
                        text: str = None,
                        activation_time: str = None,
                        custom_tag_50: str = None,
                        is_automated: bool = None,
                        other_cl_ord_id: str = None,
                        other_price: float = None,
                        other_stop_price: float = None,
                        other_max_show: int = None,
                        other_peg_difference: float = None,
                        other_time_in_force: str = None,
                        other_expire_time: str = None,
                        other_text: str = None) -> dict:
        """
        Place a Order Cancels Order order strategy.

        OCO order strategies link 2 orders together such that if one order is filled,
        the other order is cancelled. You must provide an other parameter pertaining
        to the order linked to this one. The other must specify an action and an orderType
        which determines the other parameters that must be set. For example a Limit or Stop
        order must use the price parameter, but a Stop-Limit will require a price and a stopPrice.
        """
        return await self.session.post(
            url="/order/placeoco",
            payload={
                "accountSpec": account_spec, "accountId": account_id, "clOrdId": cl_ord_id,
                "action": action, "symbol": symbol, "orderQty": order_qty, "orderType": order_type,
                "price": price, "stopPrice": stop_price, "maxShow": max_show, "pegDifference": peg_difference,
                "timeInForce": time_in_force, "expireTime": expire_time, "text": text, "activationTime": activation_time,
                "customTag50": custom_tag_50, "isAutomated": is_automated,
                "other": {
                    "action": other_action, "clOrdId": other_cl_ord_id, "orderType": other_order_type,
                    "price": other_price, "stopPrice": other_stop_price, "maxShow": other_max_show,
                    "pegDifference": other_peg_difference, "timeInForce": other_time_in_force,
                    "expireTime": other_expire_time, "text": other_text,
                },
            },
        )

    async def place_order(self,
                          action: str,
                          symbol: str,
                          order_qty: int,
                          order_type: str,
                          account_spec: str = None,
                          account_id: int = None,
                          cl_ord_id: str = None,
                          price: float = None,
                          stop_price: float = None,
                          max_show: int = None,
                          peg_difference: float = None,
                          time_in_force: str = None,
                          expire_time: str = None,
                          text: str = None,
                          activation_time: str = None,
                          custom_tag_50: str = None,
                          is_automated: bool = None) -> dict:
        """
        Make a request to place an order.
        Depending on the order type, the parameters vary.
        """
        return await self.session.post(
            url="/order/placeorder",
            payload={
                "accountSpec": account_spec, "accountId": account_id, "clOrdId": cl_ord_id,
                "action": action, "symbol": symbol, "orderQty": order_qty, "orderType": order_type,
                "price": price, "stopPrice": stop_price, "maxShow": max_show, "pegDifference": peg_difference,
                "timeInForce": time_in_force, "expireTime": expire_time, "text": text, "activationTime": activation_time,
                "customTag50": custom_tag_50, "isAutomated": is_automated,
            },
        )

    async def place_OSO(self,
                        action: str,
                        symbol: str,
                        order_qty: int,
                        order_type: str,
                        bracket_1_action: str,
                        bracket_1_order_type: str,
                        account_spec: str = None,
                        account_id: int = None,
                        cl_ord_id: str = None,
                        price: float = None,
                        stop_price: float = None,
                        max_show: int = None,
                        peg_difference: float = None,
                        time_in_force: str = None,
                        expire_time: str = None,
                        text: str = None,
                        activation_time: str = None,
                        custom_tag_50: str = None,
                        is_automated: bool = None,
                        bracket_1_cl_order_id: str = None,
                        bracket_1_price: float = None,
                        bracket_1_stop_price: float = None,
                        bracket_1_max_show: int = None,
                        bracket_1_peg_difference: float = None,
                        bracket_1_time_in_force: str = None,
                        bracket_1_expire_time: str = None,
                        bracket_1_text: str = None,
                        bracket_2_action: str = None,
                        bracket_2_order_type: str = None,
                        bracket_2_cl_order_id: str = None,
                        bracket_2_price: float = None,
                        bracket_2_stop_price: float = None,
                        bracket_2_max_show: int = None,
                        bracket_2_peg_difference: float = None,
                        bracket_2_time_in_force: str = None,
                        bracket_2_expire_time: str = None,
                        bracket_2_text: str = None) -> dict:
        """
        Place an Order Sends Order order strategy.
        OSO orders allow for the most complex multi-bracket trading strategies.
        """
        return await self.session.post(
            url="/order/placeoso",
            payload={
                "accountSpec": account_spec, "accountId": account_id, "clOrdId": cl_ord_id,
                "action": action, "symbol": symbol, "orderQty": order_qty, "orderType": order_type,
                "price": price, "stopPrice": stop_price, "maxShow": max_show, "pegDifference": peg_difference,
                "timeInForce": time_in_force, "expireTime": expire_time, "text": text, "activationTime": activation_time,
                "customTag50": custom_tag_50, "isAutomated": is_automated,
                "bracket1": {
                    "action": bracket_1_action, "clOrdId": bracket_1_cl_order_id, "orderType": bracket_1_order_type,
                    "price": bracket_1_price, "stopPrice": bracket_1_stop_price, "maxShow": bracket_1_max_show,
                    "pegDifference": bracket_1_peg_difference, "timeInForce": bracket_1_time_in_force,
                    "expireTime": bracket_1_expire_time, "text": bracket_1_text,
                },
                "bracket2": {
                    "action": bracket_2_action, "clOrdId": bracket_2_cl_order_id, "orderType": bracket_2_order_type,
                    "price": bracket_2_price, "stopPrice": bracket_2_stop_price, "maxShow": bracket_2_max_show,
                    "pegDifference": bracket_2_peg_difference, "timeInForce": bracket_2_time_in_force,
                    "expireTime": bracket_2_expire_time, "text": bracket_2_text,
                },
            },
        )

    async def order_strategy_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of OrderStrategy type related to Account entity."""
        return await self.session.get(f"/orderStrategy/deps?masterid={master_id}")

    async def interrupt_order_strategy(self, order_strategy_id: int) -> dict:
        """Stop a running multi-bracket strategy."""
        return await self.session.post(
            url="/orderStrategy/interruptorderstrategy",
            payload={"orderStrategyId": order_strategy_id},
        )

    async def order_strategy_item(self, id: int) -> dict:
        """Retrieves an entity of OrderStrategy type by its id."""
        return await self.session.get(f"/orderStrategy/item?id={id}")

    async def order_strategy_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of OrderStrategy type by its ids."""
        return await self.session.get(
            f"/orderStrategy/items?ids={','.join([str(id) for id in ids])}",
        )

    async def order_strategy_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of OrderStrategy type related to multiple entities of Account type."""
        return await self.session.get(
            f"/orderStrategy/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def order_strategy_list(self) -> dict:
        """Retrieves all entities of OrderStrategy type."""
        return await self.session.get("/orderStrategy/list")

    async def modify_order_strategy(self,
                                    order_strategy_id: int,
                                    command: str,
                                    custom_tag_50: str = None) -> dict:
        """Modify the order strategy used for an existing order."""
        return await self.session.post(
            url="/orderStrategy/modifyorderstrategy",
            payload={
                "orderStrategyId": order_strategy_id,
                "command": command,
                "customTag50": custom_tag_50,
            },
        )

    async def start_order_strategy(self,
                                   symbol: str,
                                   order_strategy_type_id: int,
                                   action: str,
                                   account_id: int = None,
                                   account_spec: str = None,
                                   params: str = None,
                                   uuid: str = None,
                                   custom_tag_50: str = None) -> dict:
        """
        Start a multi-bracket trading strategy.

        This endpoint is used with a WebSocket.

        You can create any number of brackets and
        add them to brackets field on the params
        object as a JSON string.
        """
        return await self.session.post(
            url="/orderStrategy/startorderstrategy",
            payload={
                "accountId": account_id,
                "accountSpec": account_spec,
                "symbol": symbol,
                "orderStrategyTypeId": order_strategy_type_id,
                "action": action,
                "params": params,
                "uuid": uuid,
                "customTag50": custom_tag_50,
            },
        )

    async def order_strategy_link_item(self, id: int) -> dict:
        """Retrieves an entity of OrderStrategyLink type by its id."""
        return await self.session.get(f"/orderStrategyLink/item?id={id}")

    async def order_strategy_link_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of OrderStrategyLink type by its ids."""
        return await self.session.get(
            f"/orderStrategyLink/items?ids={','.join([str(id) for id in ids])}",
        )

    async def order_strategy_link_L_dependents(self, master_ids: list[int]) -> dict:
        """"Retrieves all entities of OrderStrategyLink type related to multiple entities of OrderStrategy type"""
        return await self.session.get(
            f"/orderStrategyLink/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def order_strategy_link_list(self) -> dict:
        """Retrieves all entities of OrderStrategyLink type."""
        return await self.session.get("/orderStrategyLink/list")

    async def order_version_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of OrderVersion type related to Order entity."""
        return await self.session.get(f"/orderVersion/deps?masterid={master_id}")

    async def order_version_item(self, id: int) -> dict:
        """Retrieves an entity of OrderVersion type by its id."""
        return await self.session.get(f"/orderVersion/items?id={id}")

    async def order_version_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of OrderVersion type by its ids."""
        return await self.session.get(
            f"/orderVersion/items?ids={','.join([str(id) for id in ids])}",
        )

    async def order_version_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of OrderVersion type related to multiple entities of Order type."""
        return await self.session.get(
            f"/orderVersion/masterids={','.join([str(id) for id in master_ids])}",
        )

    async def order_version_list(self) -> dict:
        """Retrieves all entities of OrderVersion type."""
        return await self.session.get("/orderVersion/list")
