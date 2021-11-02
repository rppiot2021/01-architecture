# SCADA architecture

Example of a SCADA-like console application, used to serve as a minimal example
of a standard architecture of an IIoT system.

Install the requirements by calling:
```shell
pip install -r requirements.txt
```

The industrial process, three ammeters that measure electricity, is simulated
through the `simulator` package. To start the simulator, call:

```shell
python -m simulator.main
```

The simulator starts an IEC104 slave hosted on address `127.0.0.1` at port
`9999`. A separate package needs to be implemented, that would connect to the
simulator and print the simulated data on console output. The simulator
registers measurement changes on different protocol-specific addresses (ASDU),
which serve as identifiers of ammeters.

Also, the implemented app needs to add together the three measured currents and
display that as an additional measurement.
