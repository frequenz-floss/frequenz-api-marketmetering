# Frequenz Market Metering API Release Notes

## Summary

This release extends the `MarketLocationIdType` and `MarketArea` enum, and improves the `MarketLocationOperationResult`.

## Upgrading

- Extends `MarketArea` with new jurisdictions and clustered by geographic region
- Extends `MarketLocationIdType` by introducing new external market identifiers
- Extends `MarketLocationUpdate` to require latest revision number to be 
  provided

## New Features

- **Market Location Lifecycle**: `Activate` and `Deactivate` operations now return the new `revision` number in `MarketLocationOperationResult`.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
