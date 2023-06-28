# adaptwms
Lightweight OpenStreetMap adapter for WMS services

## What it is?

Basically it is adapter translating requests in so called
[Slippy Map format](https://wiki.openstreetmap.org/wiki/Slippy_map) (used by
OpenStreetMap, takes zoom level and XY tile indexes) into requests to external
WMS service (takes bounding box in form of two points in some coordinate
system of area to render).

To give an example , let's say you need to supply to external map viewer an URL in format:

```
https://tile.openstreetmap.org/{z}/{x}/{y}.png
```

All x,y and z are natural numbers. But the service you want to access gives you interface that requires this format:

```
https://external.service/wms?BBOX=0.0%2C0.0%2C1.0%2C1.0&SRS=EPSG%3A3857&WIDTH=256&HEIGHT=256&SERVICE=WMS
```

However it this case BBOX contains set of 4 floating point numbers for 2 (x<sub>0</sub>, y<sub>0</sub>) and (x<sub>1</sub>, y<sub>1</sub>) points limiting the area to render. This is a kind of problems this program is trying to solve.

## What is supported?

These are the known constraints:
- WMS service you use must allow unauthenticated access (there is no way for passing credentials in any form at the moment)
- it must support **EPSG:3857** coordinate system

## How to use it?

1. Make sure you have Python and pip installed
