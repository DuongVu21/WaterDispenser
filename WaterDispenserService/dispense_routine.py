from flow_meter import FlowMeter
from pump import Pump
from solenoid_valve import SV

class Dispense():
    def __init__(self, volume):
        self.pump = Pump()
        self.sv = SV()
        self.fm = FlowMeter()
        self.dispenseVolume = volume

    def start(self):
        self.pump.on()
        self.sv.open()
        self.flowRate, self.totalVolume, self.elapsedTime = self.fm.getFlowRate()
        while self.totalVolume < self.dispenseVolume:
            self.flowRate, self.totalVolume, self.elapsedTime = self.fm.getFlowRate()
            print("\nFlowrate: ", self.flowRate, "L/s")
            print("Volume: ", self.totalVolume, "L")
            print("Elapsed time: ", self.elapsedTime, "secs")
        self.pump.off()
        self.sv.close()