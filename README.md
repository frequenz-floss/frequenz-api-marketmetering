# Frequenz Market Metering API

[![Build Status](https://github.com/frequenz-floss/frequenz-api-marketmetering/actions/workflows/ci.yaml/badge.svg)](https://github.com/frequenz-floss/frequenz-api-marketmetering/actions/workflows/ci.yaml)
[![PyPI Package](https://img.shields.io/pypi/v/frequenz-api-marketmetering)](https://pypi.org/project/frequenz-api-marketmetering/)
[![Docs](https://img.shields.io/badge/docs-latest-informational)](https://frequenz-floss.github.io/frequenz-api-marketmetering/)

## Introduction

Frequenz gRPC API to retrieve data from regulated market metering points.

## API Overview

The API is defined in a single proto file:
[`marketmetering.proto`](https://github.com/frequenz-floss/frequenz-api-marketmetering/blob/v0.x.x/proto/frequenz/api/marketmetering/v1alpha1/marketmetering.proto)

### Service: `MarketMeteringService`

| RPC | Type | Description |
|-----|------|-------------|
| `CreateMarketLocation` | Unary | Register a new market location |
| `UpdateMarketLocation` | Unary | Update fields (optimistic concurrency via `expected_revision`) |
| `DeactivateMarketLocation` | Unary | Deactivate one or more locations (batch) |
| `ActivateMarketLocation` | Unary | Re-activate one or more locations (batch) |
| `ListMarketLocations` | Unary | List/filter locations with pagination |
| `UpsertMarketLocationSamplesStream` | Bidirectional streaming | Ingest samples (one per message, each gets an ack) |
| `ReceiveMarketLocationSamplesStream` | Server streaming | Subscribe to time-series data, optionally real-time |

### Key Concepts

- **MarketLocationRef** uniquely identifies a location: `enterprise_id` + `MarketLocationId` (value + type like `MALO_ID`, `MPAN`, `EAN`, etc.)
- **MarketArea** specifies jurisdiction (e.g. `EU_DE`, `NA_US_ERCOT`, `AP_JP`)
- **Samples** carry a `value`, `quality` (`MEASURED`/`ESTIMATED`/`CORRECTED`/`MISSING`), and a `revision` number for correction semantics
- **Directions**: `IMPORT` (consumption) / `EXPORT` (feed-in)
- **Metrics**: `ACTIVE_ENERGY`, `ACTIVE_POWER`, `REACTIVE_ENERGY`, `REACTIVE_POWER` with matching units

### Examples

**CreateMarketLocation** — register a new location:

```jsonc
// → Request
{
  "market_location_ref": {
    "enterprise_id": 42,
    "market_location_id": {
      "value": "50252808033",
      "type": "MARKET_LOCATION_ID_TYPE_MALO_ID"
    }
  },
  "market_location": {
    "display_name": "Solar Park Alpha",
    "market_area": "MARKET_AREA_EU_DE",
    "supported_directions": [
      "ENERGY_FLOW_DIRECTION_IMPORT",
      "ENERGY_FLOW_DIRECTION_EXPORT"
    ],
    "time_resolution": "TIME_RESOLUTION_15_MIN"
  }
}

// ← Response
{
  "enterprise_id": 42,
  "market_location": {
    "market_location_ref": {
      "enterprise_id": 42,
      "market_location_id": {
        "value": "50252808033",
        "type": "MARKET_LOCATION_ID_TYPE_MALO_ID"
      }
    },
    "market_location": {
      "display_name": "Solar Park Alpha",
      "market_area": "MARKET_AREA_EU_DE",
      "supported_directions": [
        "ENERGY_FLOW_DIRECTION_IMPORT",
        "ENERGY_FLOW_DIRECTION_EXPORT"
      ],
      "time_resolution": "TIME_RESOLUTION_15_MIN"
    },
    "revision": 1,
    "is_active": true,
    "create_time": "2025-06-01T10:00:00Z",
    "update_time": "2025-06-01T10:00:00Z"
  }
}
```

**UpsertMarketLocationSamplesStream** — ingest samples (bidirectional, each message gets an ack):

```jsonc
// → Request (one per stream message)
{
  "market_location_ref": {
    "enterprise_id": 42,
    "market_location_id": {
      "value": "50252808033",
      "type": "MARKET_LOCATION_ID_TYPE_MALO_ID"
    }
  },
  "direction": "ENERGY_FLOW_DIRECTION_IMPORT",
  "metric_type": "METRIC_TYPE_ACTIVE_ENERGY",
  "metric_unit": "METRIC_UNIT_KWH",
  "sample": {
    "sample_time": "2025-06-01T12:00:00Z",
    "value": 123.45,
    "quality": "DATA_QUALITY_MEASURED",
    "revision": 1
  }
}

// ← Response (one ack per sample — echoes back ref + sample)
{
  "market_location_ref": { "..." : "echoed from request" },
  "sample": { "...": "echoed from request" },
  "ingest_time": "2025-06-01T12:00:01Z",
  "success": true,
  "error_code": "...",    // only on failure
  "error_message": "..."  // only on failure
}
```

**ReceiveMarketLocationSamplesStream** — subscribe to time-series (server streaming, stays open if no `end_time`):

```jsonc
// → Request
{
  "market_location_refs": [
    {
      "enterprise_id": 42,
      "market_location_id": {
        "value": "50252808033",
        "type": "MARKET_LOCATION_ID_TYPE_MALO_ID"
      }
    }
  ],
  "directions": ["ENERGY_FLOW_DIRECTION_IMPORT"],
  "metric_types": ["METRIC_TYPE_ACTIVE_ENERGY"]
}

// ← Response (streamed fragments)
{
  "stream_filter": {
    "revision_strategy": "REVISION_STRATEGY_LATEST_ONLY",
    "resampling_options": {
      "resolution": "TIME_RESOLUTION_15_MIN"
    }
  },
  "series": [
    {
      "market_location_ref": {
        "enterprise_id": 42,
        "market_location_id": {
          "value": "50252808033",
          "type": "MARKET_LOCATION_ID_TYPE_MALO_ID"
        }
      },
      "direction": "ENERGY_FLOW_DIRECTION_IMPORT",
      "metric_type": "METRIC_TYPE_ACTIVE_ENERGY",
      "metric_unit": "METRIC_UNIT_KWH",
      "resolution": "TIME_RESOLUTION_15_MIN",
      "samples": [
        {
          "sample_time": "2025-06-01T12:00:00Z",
          "value": 1.234,
          "quality": "DATA_QUALITY_MEASURED",
          "revision": 1,
          "sample_update_time": "2025-06-01T12:00:02Z",
          "resampling_method": "RESAMPLING_METHOD_NATIVE"
        },
        {
          "sample_time": "2025-06-01T12:15:00Z",
          "value": 0.987,
          "quality": "DATA_QUALITY_MEASURED",
          "revision": 1,
          "sample_update_time": "2025-06-01T12:15:02Z",
          "resampling_method": "RESAMPLING_METHOD_NATIVE"
        }
      ]
    }
  ]
}
```

## Supported Platforms

The following platforms are officially supported (tested):

- **Python:** 3.11
- **Operating System:** Ubuntu Linux 20.04
- **Architectures:** amd64, arm64

## Contributing

If you want to know how to build this project and contribute to it, please
check out the [Contributing Guide](CONTRIBUTING.md).
