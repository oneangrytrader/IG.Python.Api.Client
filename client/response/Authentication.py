from dataclasses import dataclass
from client.helper.TypeConverter import *
from client.model.AccountInfo import AccountInfo
from client.model.AuthenticationAccount import AuthenticationAccount


@dataclass
class Authentication:
    account_type: str
    account_info: AccountInfo
    currency_iso_code: str
    currency_symbol: str
    current_account_id: str
    lightstreamer_endpoint: str
    accounts: List[AuthenticationAccount]
    client_id: int
    timezone_offset: int
    has_active_demo_accounts: bool
    has_active_live_accounts: bool
    trailing_stops_enabled: bool
    rerouting_environment: None
    dealing_enabled: bool
    token: str
    api_key: str
    cst: str

    @staticmethod
    def from_dict(obj: Any) -> 'Authentication':
        assert isinstance(obj, dict)
        account_type = from_str(obj.get("accountType"))
        account_info = AccountInfo.from_dict(obj.get("accountInfo"))
        currency_iso_code = from_str(obj.get("currencyIsoCode"))
        currency_symbol = from_str(obj.get("currencySymbol"))
        current_account_id = from_str(obj.get("currentAccountId"))
        lightstreamer_endpoint = from_str(obj.get("lightstreamerEndpoint"))
        accounts = from_list(AuthenticationAccount.from_dict, obj.get("accounts"))
        client_id = int(from_str(obj.get("clientId")))
        timezone_offset = from_int(obj.get("timezoneOffset"))
        has_active_demo_accounts = from_bool(obj.get("hasActiveDemoAccounts"))
        has_active_live_accounts = from_bool(obj.get("hasActiveLiveAccounts"))
        trailing_stops_enabled = from_bool(obj.get("trailingStopsEnabled"))
        rerouting_environment = from_none(obj.get("reroutingEnvironment"))
        dealing_enabled = from_bool(obj.get("dealingEnabled"))
        return Authentication(account_type, account_info, currency_iso_code, currency_symbol, current_account_id,
                              lightstreamer_endpoint, accounts, client_id, timezone_offset, has_active_demo_accounts,
                              has_active_live_accounts, trailing_stops_enabled, rerouting_environment, dealing_enabled)

    def to_dict(self) -> dict:
        result: dict = {"accountType": from_str(self.account_type),
                        "accountInfo": to_class(AccountInfo, self.account_info),
                        "currencyIsoCode": from_str(self.currency_iso_code),
                        "currencySymbol": from_str(self.currency_symbol),
                        "currentAccountId": from_str(self.current_account_id),
                        "lightstreamerEndpoint": from_str(self.lightstreamer_endpoint),
                        "accounts": from_list(lambda x: to_class(AuthenticationAccount, x), self.accounts),
                        "clientId": from_str(str(self.client_id)), "timezoneOffset": from_int(self.timezone_offset),
                        "hasActiveDemoAccounts": from_bool(self.has_active_demo_accounts),
                        "hasActiveLiveAccounts": from_bool(self.has_active_live_accounts),
                        "trailingStopsEnabled": from_bool(self.trailing_stops_enabled),
                        "reroutingEnvironment": from_none(self.rerouting_environment),
                        "dealingEnabled": from_bool(self.dealing_enabled)}
        return result


def authentication_from_dict(s: Any) -> Authentication:
    return Authentication.from_dict(s)


def authentication_to_dict(x: Authentication) -> Any:
    return to_class(Authentication, x)
