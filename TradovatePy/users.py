class Users:

    def __init__(self, session) -> None:
        """User's constructor."""
        self.session = session

    async def contract_info_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of ContactInfo type related to User entity."""
        return self.session.get(f"/contractInfo/deps?masterid={master_id}")

    async def contract_info_item(self, id: int) -> dict:
        """Retrieves an entity of ContactInfo type by its id."""
        return self.session.get(f"/contractInfo/item?id={id}")

    async def contract_info_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of ContactInfo type by its ids."""
        return self.session.get(
            f"/contractInfo/items?ids={','.join([str(id) for id in ids])}",
        )

    async def contract_info_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of ContactInfo type related to multiple entities of User type."""
        return self.session.get(
            f"/contractInfo/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def market_data_subscription_create(self,
                                              user_id: int,
                                              plan_price: float,
                                              market_data_sub_plan_id: int,
                                              timestamp: str,
                                              year: int,
                                              month: int,
                                              id: int = None,
                                              credit_card_transaction_id: int = None,
                                              cash_balance_log_id: int = None,
                                              credit_card_id: int = None,
                                              account_id: int = None,
                                              renewal_credit_card_id: int = None,
                                              renewal_account_id: int = None) -> dict:
        """Creates a new entity of MarketDataSubscription."""
        return self.session.post(
            url="/marketDataSubscription/create",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id,
                "accountId": account_id, "MarketDataSubscriptionPlanId": market_data_sub_plan_id,
                "year": year, "month": month, "renewalCreditCardId": renewal_credit_card_id,
                "renewalAccountId": renewal_account_id,
            },
        )

    async def market_data_subscription_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of MarketDataSubscription type related to User entity."""
        return self.session.get(f"/marketDataSubscription/deps?masterid={master_id}")

    async def market_data_subscription_item(self, id: int) -> dict:
        """Retrieves an entity of MarketDataSubscription type by its id."""
        return self.session.get(f"/marketDataSubscription/item?id={id}")

    async def market_data_subscription_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of MarketDataSubscription type by its ids."""
        return self.session.get(
            f"/marketDataSubscription/items?ids={','.join([str(id) for id in ids])}",
        )

    async def market_data_subscription_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of MarketDataSubscription type related to multiple entities of User type."""
        return self.session.get(
            f"/marketDataSubscription/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def market_data_subscription_list(self) -> dict:
        """Retrieves all entities of MarketDataSubscription type."""
        return self.session.get("/marketDataSubscription/list")

    async def market_data_subscription_update(self,
                                              user_id: int,
                                              timestamp: str,
                                              plan_price: float,
                                              market_data_sub_plan_id: int,
                                              year: int,
                                              month: int,
                                              id: int = None,
                                              credit_card_transaction_id: int = None,
                                              cash_balance_log_id: int = None,
                                              credit_card_id: int = None,
                                              account_id: int = None,
                                              renewal_credit_card_id: int = None,
                                              renewal_account_id: int = None) -> dict:
        """Updates an existing entity of MarketDataSubscription."""
        return await self.session.post(
            url="/marketDataSubscription/update",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id,
                "accountId": account_id, "marketDataSubscriptionPlanId": market_data_sub_plan_id,
                "year": year, "month": month, "renewalCreditCardId": renewal_credit_card_id,
                "renewalAccountId": renewal_account_id,
            },
        )

    async def organization_find(self, name: str) -> dict:
        """Retrieves an entity of Organization type by its name."""
        return await self.session.get(f"/organization/find?name={name}")

    async def organization_item(self, id: int) -> dict:
        """Retrieves an entity of Organization type by its id."""
        return await self.session.get(f"/organization/item?id={id}")

    async def organization_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of Organization type by its ids."""
        return await self.session.get(
            f"/organization/ids={','.join([str(id) for id in ids])}",
        )

    async def organization_list(self) -> dict:
        """Retrieves all entities of Organization type."""
        return await self.session.get("/organization/list")

    async def organization_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of Organization type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/organization/suggest?t={text}&l={n_entities}")

    async def second_market_data_subscription_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of SecondMarketDataSubscription type related to User entity."""
        return await self.session.get(f"/secondMarketDataSubscription/deps?masterid={master_id}")

    async def second_market_data_subscription_item(self, id: int) -> dict:
        """Retrieves an entity of SecondMarketDataSubscription type by its id."""
        return await self.session.get(f"/secondMarketDataSubscription/item?id={id}")

    async def second_market_data_subscription_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of SecondMarketDataSubscription type by its ids."""
        return await self.session.get(
            f"/secondMarketDataSubscription/items?ids={','.join([str(id) for id in ids])}",
        )

    async def second_market_data_subscription_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of SecondMarketDataSubscription type related to multiple entities of User type."""
        return await self.session.get(
            f"/secondMarketDataSubscription/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def second_market_data_subscription_list(self) -> dict:
        """Retrieves all entities of SecondMarketDataSubscription type."""
        return await self.session.get("/secondMarketDataSubscription/list")

    async def tradovate_subscription_create(self,
                                            user_id: int,
                                            timestamp: str,
                                            plan_price: float,
                                            tradovate_subscription_plan_id: int,
                                            start_date: str,
                                            expiration_date: str,
                                            paid_amount: float,
                                            id: int = None,
                                            credit_card_transaction_id: int = None,
                                            cash_balance_log_id: int = None,
                                            credit_card_id: int = None,
                                            account_id: int = None,
                                            cancelled_renewal: bool = None,
                                            cancel_reason: str = None) -> dict:
        """Creates a new entity of TradovateSubscription."""
        return await self.session.post(
            url="/tradovateSubscription/create",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id,
                "accountId": account_id, "tradovateSubscriptionPlanId": tradovate_subscription_plan_id,
                "startDate": start_date, "expirationDate": expiration_date, "paidAmount": paid_amount,
                "cancelledRenewal": cancelled_renewal, "cancelReason": cancel_reason,
            },
        )

    async def tradovate_subscription_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of SecondMarketDataSubscription type related to multiple entities of User type."""
        return await self.session.get(f"/tradovateSubscription/deps?masterid={master_id}")

    async def tradovate_subscription_item(self, id: int) -> dict:
        """Retrieves an entity of TradovateSubscription type by its id."""
        return await self.session.get(f"/tradovateSubscription/item?id={id}")

    async def tradovate_subscription_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of TradovateSubscription type by its ids."""
        return await self.session.get(
            f"/tradovateSubscription/items?ids={','.join([str(id) for id in ids])}",
        )

    async def tradovate_subscription_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of TradovateSubscription type related to multiple entities of User type."""
        return await self.session.get(
            f"/tradovateSubscription/ldeps?masterids={master_ids}",
        )

    async def tradovate_subscription_list(self) -> dict:
        """Retrieves all entities of TradovateSubscription type."""
        return await self.session.get("/tradovateSubscription/list")

    async def tradovate_subscription_update(self,
                                            user_id: int,
                                            timestamp: str,
                                            plan_price: float,
                                            tradovate_subscription_plan_id: int,
                                            start_date: dict,
                                            expiration_date: dict,
                                            paid_amount: float,
                                            id: int = None,
                                            credit_card_transaction_id: int = None,
                                            cash_balance_log_id: int = None,
                                            credit_card_id: int = None,
                                            account_id: int = None,
                                            cancelled_renewal: bool = None,
                                            cancel_reason: str = None) -> dict:
        """Updates an existing entity of TradovateSubscription."""
        return await self.session.post(
            url="/tradovateSubscription/update",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id,
                "accountId": account_id, "tradovateSubscriptionPlanId": tradovate_subscription_plan_id,
                "startDate": start_date, "expirationDate": expiration_date, "paidAmount": paid_amount,
                "cancelledRenewal": cancelled_renewal, "cancelReason": cancel_reason,
            },
        )

    async def accept_trading_permission(self, trading_permission_id: int) -> dict:
        """Called to accept a given trading permission granted by another party."""
        return await self.session.post(
            url="/user/accepttradingpermission",
            payload={"tradingPermissionId": trading_permission_id},
        )

    async def activate_second_market_data_subscription_renewal(self, second_market_data_sub_id: int) -> dict:
        """Used to setup a second market data subscription with active auto-renewal."""
        return await self.session.post(
            url="/user/activatesecondmarketdatasubscriptionrenewal",
            payload={"secondMarketDataSubscriptionId": second_market_data_sub_id},
        )

    async def add_market_data_subscription(self,
                                           market_data_subscription_plan_ids: list[int],
                                           year: int,
                                           month: int,
                                           credit_card_id: int = None,
                                           account_id: int = None,
                                           user_id: int = None) -> dict:
        """Add a subscription to Market Data for a user."""
        return await self.session.post(
            url="/user/addmarketdatasubscription",
            payload={
                "marketDataSubscriptionPlanIds": market_data_subscription_plan_ids,
                "year": year, "month": month, "creditCardId": credit_card_id,
                "accountId": account_id, "userId": user_id,
            },
        )

    async def add_second_market_data_subscription(self,
                                                  year: int,
                                                  month: int,
                                                  credit_card_id: int = None,
                                                  account_id: int = None,
                                                  user_id: int = None) -> dict:
        """Add a subscription to Market Data for a user."""
        return await self.session.post(
            url="/user/addmarketdatasubscription",
            payload={
                "year": year, "month": month, "creditCardId": credit_card_id,
                "accountId": account_id, "userId": user_id,
            },
        )

    async def add_tradovate_subscription(self,
                                         tradovate_subscription_plan_id: int,
                                         credit_card_id: int = None,
                                         account_id: int = None,
                                         user_id: int = None) -> dict:
        """Used to add a Tradovate Trader membership plan for a user."""
        return await self.session.post(
            url="/user/addtradovatesubscription",
            payload={
                "tradovateSubscriptionPlanId": tradovate_subscription_plan_id,
                "creditCardId": credit_card_id, "accountId": account_id, "userId": user_id,
            },
        )

    async def cancel_second_market_data_subscription(self, second_market_data_sub_id: int) -> dict:
        """Cancel a second market data subscription for a user."""
        return await self.session.post(
            url="",
            payload={
                "secondMarketDataSubscriptionId": second_market_data_sub_id,
            },
        )

    async def cancel_second_market_data_subscription_renewal(self, second_market_data_sub_id: int) -> dict:
        """Cancel the auto-renewal for a second market data subscription for a user."""
        return self.session.post(
            url="/user/cancelsecondmarketdatasubscriptionrenewal",
            payload={
                "secondMarketDataSubscriptionId": second_market_data_sub_id,
            },
        )

    async def cancel_tradovate_subscription(self,
                                            tradovate_sub_id: int,
                                            cancel_reason: str = None,
                                            expire: bool = None) -> dict:
        """Cancel a Tradovate Trader membership plan."""
        return await self.session.post(
            url="/user/canceltradovatesubscription",
            payload={
                "tradovateSubscriptionId": tradovate_sub_id, "cancelReason": cancel_reason,
                "expire": expire,
            },
        )

    async def user_find(self, name: str) -> dict:
        """Retrieves an entity of User type by its name."""
        return await self.session.get(f"/user/find?name={name}")

    async def get_account_trading_permissions(self, account_id: int) -> dict:
        """Query the granted trading permissions associated with this account."""
        return await self.session.post(
            url="/user/getaccounttradingpermissions",
            payload={"accountId": account_id},
        )

    async def get_second_market_data_subscription_cost(self,
                                                       year: int,
                                                       month: int,
                                                       user_id: int = None) -> dict:
        """Query the current price of a second market data subscription for a user."""
        return await self.session.post(
            url="/user/getsecondmarketdatasubscriptioncost",
            payload={
                "year": year, "month": month, "userId": user_id,
            },
        )

    async def user_item(self, id: int) -> dict:
        """Retrieves an entity of User type by its id."""
        return await self.session.get(f"/user/item?id={id}")

    async def user_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of User type by its ids."""
        return await self.session.get(
            f"/user/items?ids={','.join([str(id) for id in ids])}",
        )

    async def user_list(self) -> dict:
        """Retrieves all entities of User type."""
        return await self.session.get("/user/list")

    async def modify_credentials(self,
                                 name: str,
                                 new_password: str,
                                 current_password: str,
                                 user_id: int = None) -> dict:
        """Used to modify account username and password."""
        return await self.session.post(
            url="/user/modifycredentials",
            payload={
                "userId": user_id, "name": name, "password": new_password,
                "currentPassword": current_password, "userId": user_id,
            },
        )

    async def modify_email_address(self,
                                   email: str,
                                   user_id: int) -> dict:
        """Change account email address information."""
        return await self.session.post(
            url="/user/modifyemailaddress",
            payload={
                "userId": user_id, "email": email,
            },
        )

    async def modify_password(self,
                              password: str,
                              current_password: str,
                              user_id: int) -> dict:
        """Change account password information."""
        return await self.session.post(
            url="/user/modifypassword",
            payload={
                "userId": user_id, "password": password, "currentPassword": current_password,
            },
        )

    async def open_demo_account(self,
                                template_account_id: int = None,
                                name: str = None,
                                initial_balance: float = None) -> dict:
        """Request to open a Demo account for a user."""
        return await self.session.post(
            url="/user/opendemoaccount",
            payload={
                "templateAccountId": template_account_id, "name": name, "initialBalance": initial_balance,
            },
        )

    async def request_trading_permission(self,
                                         account_id: int,
                                         cta_contact: str,
                                         cta_email: str) -> dict:
        """
        Send a request to grant trading permission for your account to another party.

        Once this request is reviewed by our accounting and compliance, the other party
        will be allowed to access your account as if it was one of that party's own accounts.
        """
        return await self.session.post(
            url="/user/requesttradingpermission",
            payload={
                "accountId": account_id, "ctaContact": cta_contact, "ctaEmail": cta_email,
            },
        )

    async def revoke_trading_permissions(self, trading_permission_id: int) -> dict:
        """
        Revoke an existing trading permission granted to another party.

        If a user wants to end the terms of a granted permission to trade using your account,
        a user can revoke those permissions using this endpoint.
        """
        return await self.session.post(
            url="/user/revoketradingpermissions",
            payload={"tradingPermissionId": trading_permission_id},
        )

    async def sign_up_organization_member(self, name: str,
                                          email: str, password: str,
                                          first_name: str, last_name: str) -> dict:
        """Used by B2B partners to create users for their own organizations."""
        return await self.session.post(
            url="/user/signuporganizationmember",
            payload={
                "name": name, "email": email, "password": password,
                "firstName": first_name, "lastName": last_name,
            },
        )

    async def user_suggest(self, text: str, n_entities: int) -> dict:
        """Retrieves entities of User type filtered by an occurrence of a text in one of its fields."""
        return await self.session.get(f"/user/suggest?t={text}&n_entities={n_entities}")

    async def sync_request(self,
                           users: list[int] = None,
                           accounts: list[int] = None,
                           split_responses: bool = None) -> dict:
        """
        Used with WebSocket protocol. Returns all data associated with the user.
        This endpoint is essential for efficient use of the WebSocket API.
        """
        return await self.session.post(
            url="/user/syncrequest",
            payload={
                "users": users, "accounts": accounts, "splitResponses": split_responses,
            },
        )

    async def add_entitlement_subscription(self,
                                           entitlement_id: int,
                                           credit_card_id: int = None,
                                           account_id: int = None,
                                           user_id: int = None) -> dict:
        """For use with Add-ons, allows for purchase of entitlements such as Market Replay."""
        return await self.session.post(
            url="/userPlugin/addentitlementsubscription",
            payload={
                "entitlementId": entitlement_id, "creditCardId": credit_card_id,
                "accountId": account_id, "userId": user_id,
            },
        )

    async def change_plugin_permission(self,
                                       pluginName: str,
                                       approval: bool,
                                       user_id: int = None) -> dict:
        """Change the permissions for a Trader plugin."""
        return await self.session.post(
            url="/userPlugin/changepermission",
            payload={
                "userId": user_id, "pluginName": pluginName,
                "approval": approval,
            },
        )

    async def user_plugin_create(self,
                                 user_id: int,
                                 timestamp: str,
                                 plan_price: float,
                                 plugin_name: str,
                                 apporval: bool,
                                 start_date: dict,
                                 paid_amount: float,
                                 credit_card_transaction_id: int = None,
                                 cash_balance_log_id: int = None,
                                 credit_card_id: int = None,
                                 account_id: int = None,
                                 id: int = None,
                                 entitlement_id: int = None,
                                 expiration_date: dict = None,
                                 auto_renewal: bool = None,
                                 plan_categories: str = None) -> dict:
        """Creates a new entity of UserPlugin."""
        return self.session.post(
            url="/userPlugin/create",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id, "accountId": account_id,
                "pluginName": plugin_name, "apporval": apporval, "entitlementId": entitlement_id,
                "startDate": start_date, "expirationDate": expiration_date, "paidAmount": paid_amount,
                "autorenewal": auto_renewal, "planCategories": plan_categories,
            },
        )

    async def user_plugin_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of UserPlugin type related to User entity."""
        return await self.session.get(f"/userPlugin/deps?masterid={master_id}")

    async def user_plugin_item(self, id: int) -> dict:
        """Retrieves an entity of UserPlugin type by its id."""
        return await self.session.get(f"/userPlugin/item?id={id}")

    async def user_plugin_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of UserPlugin type by its ids."""
        return await self.session.get(
            f"/userPlugin/items?ids={','.join([str(id) for id in ids])}",
        )

    async def user_plugin_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of UserPlugin type related to multiple entities of User type."""
        return await self.session.get(
            f"/userPlugin/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def user_plugin_list(self) -> dict:
        """Retrieves all entities of UserPlugin type."""
        return await self.session.get("/userPlugin/list")

    async def user_plugin_update(self,
                                 user_id: int,
                                 timestamp: str,
                                 plan_price: float,
                                 plugin_name: str,
                                 approval: bool,
                                 start_date: dict,
                                 paid_amount: float,
                                 id: int = None,
                                 credit_card_transaction_id: int = None,
                                 cash_balance_log_id: int = None,
                                 credit_card_id: int = None,
                                 account_id: int = None,
                                 entitlement_id: int = None,
                                 expiration_date: dict = None,
                                 auto_renewal: bool = None,
                                 plan_categories: str = None) -> dict:
        """Updates an existing entity of UserPlugin."""
        return await self.session.post(
            url="/userPlugin/update",
            payload={
                "id": id, "userId": user_id, "timestamp": timestamp,
                "planPrice": plan_price, "creditCardTransactionId": credit_card_transaction_id,
                "cashBalanceLogId": cash_balance_log_id, "creditCardId": credit_card_id,
                "accountId": account_id, "pluginName": plugin_name, "approval": approval,
                "entitlementId": entitlement_id, "startDate": start_date, "expirationDate": expiration_date,
                "paidAmount": paid_amount, "autoRenewal": auto_renewal, "planCategories": plan_categories,
            },
        )

    async def user_property_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of UserProperty type related to User entity."""
        return await self.session.get(f"/userProperty/deps?masterid={master_id}")

    async def user_property_item(self, id: int) -> dict:
        """Retrieves multiple entities of UserProperty type by its ids."""
        return await self.session.get(f"/userProperty/item?id={id}")

    async def user_property_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of UserProperty type by its ids."""
        return await self.session.get(
            f"/userProperty/items?ids={','.join([str(id) for id in ids])}",
        )

    async def user_property_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of UserProperty type related to multiple entities of User type."""
        return await self.session.get(
            f"/userProperty/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def user_session_item(self, id: int) -> dict:
        """Retrieves an entity of UserSession type by its id."""
        return await self.session.get(f"/userSession/item?id={id}")

    async def user_session_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of UserSession type by its ids."""
        return await self.session.get(
            f"/userSession/items?ids={','.join(str(id) for id in ids)}",
        )

    async def user_session_stats_dependents(self, master_id: int) -> dict:
        """Retrieves all entities of UserSessionStats type related to User entity."""
        return await self.session.get(f"/userSessionStats/deps?masterid={master_id}")

    async def user_session_stats_item(self, id: int) -> dict:
        """Retrieves an entity of UserSessionStats type by its id."""
        return await self.session.get(f"/userSessionStats/item?id={id}")

    async def user_session_stats_items(self, ids: list[int]) -> dict:
        """Retrieves multiple entities of UserSessionStats type by its ids."""
        return await self.session.get(
            f"/userSessionStats/items?ids={','.join(str(id) for id in ids)}",
        )

    async def user_session_stats_L_dependents(self, master_ids: list[int]) -> dict:
        """Retrieves all entities of UserSessionStats type related to multiple entities of User type."""
        return await self.session.get(
            f"/userSessionStats/ldeps?masterids={','.join([str(id) for id in master_ids])}",
        )

    async def user_session_stats_list(self) -> dict:
        """Retrieves all entities of UserSessionStats type."""
        return await self.session.get("/userSessionStats/list")
