# Frequenz Market Metering API Release Notes

## Summary

This is the initial release of the Market Metering API. It defines market
location lifecycle operations and revisioned metering-sample streams using the
common grid model.

## Upgrading

- Replaced `MarketLocationSelector` with `frequenz.api.common.v1alpha8.grid.MarketLocationRef`
  across Market Metering API requests and references.
- Renamed the local `MarketLocation` message to `MarketLocationMetadata`
  to distinguish descriptive metadata from the common market location identity.
- Renamed `market_location_id_filters` to `market_location_id_values`.
- Updated examples to use the new `market_location` and
  `market_location_metadata` structure.
- Bumped `frequenz-api-common` dependency to `>= 0.8.11`.

## New Features

- Added RPCs to create, update, activate, deactivate, and list market
  locations.
- Added a bidirectional stream for revisioned metering-sample upserts.
- Added a server stream for receiving revisioned or resampled metering data.
