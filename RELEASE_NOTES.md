# Frequenz Market Metering API Release Notes

## Summary

This release fixes a packaging issue and improves API consistency.

## Upgrading

**Breaking changes:**

- Enum field names in `MarketLocationIdType` renamed from `OFFICIAL_MARKET_LOCATION_ID_TYPE_*` to `MARKET_LOCATION_ID_TYPE_*`.
- Repeated field `market_location_list` renamed to `market_location_refs` in `DeactivateMarketLocationRequest`, `ActivateMarketLocationRequest`, and `ReceiveMarketLocationSamplesStreamRequest`.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

- Added missing `__init__.py` for the `v1alpha1` package, fixing wheel distribution.
