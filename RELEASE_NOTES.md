# Frequenz Market Metering API Release Notes

## Summary

This release aligns the Market Metering API with the updated common grid model.

## Upgrading

- Replaced `MarketLocationSelector` with `frequenz.api.common.v1alpha8.grid.MarketLocation`
  across Market Metering API requests and references.
- Renamed the local `MarketLocation` message to `MarketLocationMetadata`
  to distinguish descriptive metadata from the common market location identity.
- Renamed `market_location_id_filters` to `market_location_id_values`.
- Updated examples to use the new `market_location` and
  `market_location_metadata` structure.
- Bumped `frequenz-api-common` dependency to `>= 0.8.9`.

## New Features

## Bug Fixes
