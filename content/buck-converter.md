---
title: Buck Converter
date: 31/10/2026
---
A buck converter is also called a step-down converter. It's a DC-to-DC power converter. It converts a high voltage DC current into a low voltage DC current, while increasing the output current.

So, High Voltage, Low current electricity -> Goes into buck converter -> Low voltage, High current electricity comes out.

TBD the detailed design on how it works.
But on a high level it rapidly switches on and off a [MOSFET](mosfet.html) , and smoothens the current wave using capacitors, inductors, and diodes.
By controlling the fraction of time the [MOSFET](mosfet.html) switch stays on or off - it precisely regulates the average output voltage.
