# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2025-04-09T19:32:21+00:00

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Annotated, Any, List, NewType, Optional, Union

from pydantic import (
    BaseModel,
    Field,
    RootModel,
    StringConstraints,
    field_serializer,
    field_validator,
)

AddressStr = NewType("AddressStr", str)

Address = Annotated[
    AddressStr,
    StringConstraints(
        pattern=r"(^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$)|(^(0x[a-fA-F0-9]{40})$)"
    ),
]


def to_number(value) -> Decimal | None:
    try:
        return Decimal(str(value))
    except Exception:
        return None


class Error(BaseModel):
    field: str
    message: str


class UnprocessableEntity(BaseModel):
    code: int
    message: str
    errors: List[Error]


class BadRequest(BaseModel):
    code: int
    message: str


class TokenSchema(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None


class FeesResponseItem(BaseModel):
    chainId: int
    address: str
    symbol: str
    decimals: int
    value: int

    @field_validator("value", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("value")
    @classmethod
    def serialize_value(cls, v):
        return str(v)


class FeesResponseSchema(BaseModel):
    fees: list[FeesResponseItem]
    updatedAt: int


class TokensResponseSchemaItem(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None


class TokensResponseSchema(RootModel[List[TokensResponseSchemaItem]]):
    pass


class TokenAmountSchema(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class Token(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None


class RouteItemSchema(BaseModel):
    provider: str
    tokens: List[Token]


class Value(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class Save(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class FeeItemSchema(BaseModel):
    provider: str
    value: Value
    save: Optional[Save] = None
    description: Optional[str] = None


class TokenAmountIn(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class TokenOut(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None


class MiddlewareCall(BaseModel):
    address: Address
    data: str
    offset: float


class RevertableAddress(BaseModel):
    chainId: int
    address: Address


class SelectMode(str, Enum):
    BEST_RETURN = "best_return"
    FASTEST = "fastest"


class SwapRequestSchema(BaseModel):
    tokenAmountIn: TokenAmountIn
    tokenOut: TokenOut
    from_: Address = Field(..., alias="from")
    to: Address
    slippage: int
    middlewareCall: Optional[MiddlewareCall] = None
    revertableAddresses: Optional[List[RevertableAddress]] = None
    selectMode: Optional[SelectMode] = None
    partnerAddress: Optional[str] = None
    refundAddress: Optional[Address] = None

    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }


class EvmTxSchema(BaseModel):
    chainId: int
    to: Address
    data: str
    value: Optional[str] = None


class TronTxSchema(BaseModel):
    chainId: int
    from_: Address = Field(..., alias="from")
    to: Address
    data: str
    value: Optional[str] = None
    feeLimit: int
    functionSelector: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }


class Message(BaseModel):
    address: str
    amount: str
    payload: str


class TonTxSchema(BaseModel):
    validUntil: int
    messages: List[Message]


class SolanaTxSchema(BaseModel):
    instructions: str


class BtcDepositSchema(BaseModel):
    depositAddress: Address
    expiresAt: str


class Tx(BaseModel):
    chainId: int
    to: Address
    data: str
    value: Optional[str] = None


class Tx1(BaseModel):
    chainId: int
    from_: Address = Field(..., alias="from")
    to: Address
    data: str
    value: Optional[str] = None
    feeLimit: int
    functionSelector: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }


class Tx2(BaseModel):
    validUntil: int
    messages: List[Message]


class Tx3(BaseModel):
    depositAddress: Address
    expiresAt: str


class Tx4(BaseModel):
    instructions: str


class Fee(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class Fee1(BaseModel):
    provider: str
    value: Value
    save: Optional[Save] = None
    description: Optional[str] = None


class RouteItem(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None


class Route(BaseModel):
    provider: str
    tokens: List[Token]


class TokenAmountOut(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class TokenAmountOutMin(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class AmountInUsd(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class Reward(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class SwapResponseSchema(BaseModel):
    tx: Union[Tx, Tx1, Tx2, Tx3, Tx4]
    fee: Optional[Fee] = None
    fees: List[Fee1]
    route: List[RouteItem]
    routes: List[Route]
    priceImpact: str
    tokenAmountOut: TokenAmountOut
    tokenAmountOutMin: TokenAmountOutMin
    amountInUsd: AmountInUsd
    rewards: List[Reward]
    approveTo: Optional[Address] = None
    inTradeType: str
    outTradeType: str
    type: str
    kind: str
    estimatedTime: float = Field(..., description="Estimated swap time in seconds")


class SwapLimitsResponseSchemaItem(BaseModel):
    chainId: int
    address: Address | str
    min: int
    max: int


class SwapLimitsResponseSchema(RootModel[List[SwapLimitsResponseSchemaItem]]):
    pass


class SwapDurationsResponseSchemaItem(BaseModel):
    toChainId: int
    min: float
    max: float


class SwapDurationsResponseSchema(RootModel[List[SwapDurationsResponseSchemaItem]]):
    pass


class ZappingExactInRequestSchema(BaseModel):
    tokenAmountIn: TokenAmountIn
    to: Address
    from_: Address = Field(..., alias="from")
    slippage: int

    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }


class Tx5(BaseModel):
    chainId: int
    to: Address
    data: str
    value: Optional[str] = None


class Tx6(BaseModel):
    chainId: int
    from_: Address = Field(..., alias="from")
    to: Address
    data: str
    value: Optional[str] = None
    feeLimit: int
    functionSelector: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }


class Tx7(BaseModel):
    validUntil: int
    messages: List[Message]


class Tx8(BaseModel):
    depositAddress: Address
    expiresAt: str


class Tx9(BaseModel):
    instructions: str


class Fee2(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class Fee3(BaseModel):
    provider: str
    value: Value
    save: Optional[Save] = None
    description: Optional[str] = None


class Route1(BaseModel):
    provider: str
    tokens: List[Token]


class ZappingExactInResponseSchema(BaseModel):
    tx: Union[Tx5, Tx6, Tx7, Tx8, Tx9]
    fee: Optional[Fee2] = None
    fees: List[Fee3]
    route: List[RouteItem]
    routes: List[Route1]
    priceImpact: str
    tokenAmountOut: TokenAmountOut
    tokenAmountOutMin: TokenAmountOutMin
    amountInUsd: AmountInUsd
    rewards: List[Reward]
    approveTo: Optional[Address] = None
    inTradeType: str
    outTradeType: str
    type: str
    kind: str
    estimatedTime: float = Field(..., description="Estimated swap time in seconds")


class StuckedRequestSchema(BaseModel):
    address: Address


class TokenAmount(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class StuckedResponseSchemaItem(BaseModel):
    hash: str
    chainId: float
    createdAt: str
    tokenAmount: TokenAmount


class StuckedResponseSchema(RootModel[List[StuckedResponseSchemaItem]]):
    pass


class RevertRequestSchema(BaseModel):
    transactionHash: str
    chainId: float


class Tx10(BaseModel):
    chainId: int
    to: Address
    data: str
    value: Optional[str] = None


class Fee4(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class RevertResponseSchema(BaseModel):
    tx: Tx10
    fee: Fee4
    type: str


class ChainsResponseSchemaItem(BaseModel):
    id: int
    name: str
    explorer: str
    icon: str


class ChainsResponseSchema(RootModel[List[ChainsResponseSchemaItem]]):
    pass


class Status(BaseModel):
    code: float
    text: str


class Tx11(BaseModel):
    hash: str
    chainId: int
    tokenAmount: TokenAmount
    time: str
    address: str


class TxIn(BaseModel):
    hash: str
    chainId: int
    tokenAmount: TokenAmount
    time: str
    address: str


class TransitTokenSent(BaseModel):
    address: Any
    chainId: int
    chainIdFrom: Optional[int] = None
    decimals: int
    symbol: Optional[str] = None
    icon: Optional[str] = None
    amount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class TxResponseSchema(BaseModel):
    status: Status
    tx: Tx11
    txIn: TxIn
    transitTokenSent: TransitTokenSent | None


class Tx12(BaseModel):
    transactionHash: str
    chainId: float


class BatchTxRequestSchema(BaseModel):
    txs: List[Tx12]


class Tx13(BaseModel):
    hash: str
    chainId: float
    tokenAmount: TokenAmount
    time: str
    address: str


class TxIn1(BaseModel):
    hash: str
    chainId: float
    tokenAmount: TokenAmount
    time: str
    address: str


class BatchTxResponseSchemaItem(BaseModel):
    status: Status
    tx: Tx13
    txIn: TxIn1
    transitTokenSent: TransitTokenSent | None


class BatchTxResponseSchema(RootModel[List[BatchTxResponseSchemaItem]]):
    pass


class DirectRoutesResponseItem(BaseModel):
    originChainId: int
    originToken: str
    destinationChainId: int
    destinationToken: str


class DirectRoutesResponse(RootModel[List[DirectRoutesResponseItem]]):
    pass


class SwapToken(BaseModel):
    address: str
    fee_rounding: int
    decimals: int
    symbol: str
    total_limit: int | None = None
    tx_limit: int | None = None


class SwapPortal(BaseModel):
    address: str
    tokens: List[SwapToken]


class SwapConfigsResponseItem(BaseModel):
    chain_id: int
    fee: int
    portal: Optional[SwapPortal]
    block_indent: int


class SwapConfigsResponseSchema(RootModel[List[SwapConfigsResponseItem]]):
    pass


class SwapDiscountTiersResponseSchemaItem(BaseModel):
    amount: int
    discount: int

    @field_validator("amount", mode="before")
    @classmethod
    def check_value(cls, v):
        num = to_number(v)
        if num is None:
            raise ValueError(f"Value {v} is not a number")
        return int(num)

    @field_serializer("amount")
    @classmethod
    def serialize_amount(cls, v):
        return str(v)


class SwapDiscountTiersResponseSchema(
    RootModel[List[SwapDiscountTiersResponseSchemaItem]]
):
    pass


class SwapChainsResponseSchema(RootModel[List[int]]):
    pass
