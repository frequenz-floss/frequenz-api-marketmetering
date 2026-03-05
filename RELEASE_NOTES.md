# Frequenz Market Metering API Release Notes

## Summary

This release moves `market_area` from `MarketLocation` to `MarketLocationRef`,
making the jurisdiction an explicit part of the immutable identity of a Market
Location. It also extends `MarketLocationIdType` and refines documentation of
the `MarketLocationId` message.

## Upgrading

- `market_area` has been moved from `MarketLocation` to `MarketLocationRef`.
  Set and read it there in all RPCs.
- Remove misleading documentation
- Added echoing direction, metric_type and metric_unit when inserting samples
- Reworked streaming response for upserting market locations and samples.
- Remove bool success in favour of just checking if error is unset

## New Features


## Bug Fixes

- Fix docs: Remove market_area from example list for updating the revision.
<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
