# Frequenz Market Metering API Release Notes

## Summary

This release refines enterprise scoping semantics for Market Location
operations.

Enterprise ownership is now consistently derived from the caller's
authentication context for create and update operations. To support this,
the release introduces `MarketLocationSelector` as an enterprise-scoped
identifier while keeping `MarketLocationRef` as the globally unique resolved
reference.

## Upgrading

- Added `MarketLocationSelector` for enterprise-scoped Market Location
  identification.
- `CreateMarketLocationRequest` now uses
  `market_location_selector`.
- `UpdateMarketLocationRequest` now identifies Market Locations using
  `MarketLocationSelector` instead of `MarketLocationRef`.
- Create and update operations no longer require clients to explicitly provide
  an `enterprise_id`.
- Enterprise ownership is now derived from the clients's authentication context.

## New Features

- Added `MarketLocationSelector`.

## Bug Fixes

- Refined documentation around enterprise scoping and Market Location identit
