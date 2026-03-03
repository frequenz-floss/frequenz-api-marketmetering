# Frequenz Market Metering API Release Notes

## Summary

This release extends `MarketLocationIdType` and refined documentation of
`MarketLocationId` message.

## Upgrading

- Remove misleading documentation
- Added echoing direction, metric_type and metric_unit when inserting samples
- Reworked streaming response for upserting market locations and samples.
- Remove bool success in favour of just checking if error is unset

## New Features


## Bug Fixes

- Fix docs: Remove market_area from example list for updating the revision.
<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
