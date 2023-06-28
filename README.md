# adaptwms
Lightweight OpenStreetMap adapter for WMS services

## What it is?

Basically it is adapter translating requests in so called
[Slippy Map format](https://wiki.openstreetmap.org/wiki/Slippy_map) (used by
OpenStreetMap, takes zoom level and XY tile indexes) into requests to external
WMS service (takes bounding box in form of two points in some coordinate
system of area to render).

## What is supported?

These are the known constraints:
- WMS service you use must allow unauthenticated access (there is no way for passing credentials in any form at the moment)
- it must support **EPSG:3857** coordinate system

## How to use it?

1. Make sure you have Python and pip installed
